import logging
import multiprocessing
import os
import subprocess
import tempfile
from collections import defaultdict
from sqlalchemy.sql.expression import true

from binders import app, db
from binders.models.core import Repository, RepositoryOwner, RepositoryLang, Documentation, DocumentationType

config = app.config
logger = logging.getLogger(__name__)


def get_active_repo_docs():
    active_repos = db.session\
        .query(Repository, Documentation)\
        .filter(Documentation.is_active == true())\
        .all()

    repo_docs = defaultdict(list)
    for repo, doc in active_repos:
        repo_docs[(repo.name, repo.url, repo.branch)].append(doc.doc_gen_script)

    return repo_docs


def get_repo_doc_details():
    repo_details = db.session\
        .query(Repository.name,
               str(Repository.updated_at),
               RepositoryOwner.name,
               RepositoryLang.name,
               Documentation.name,
               Documentation.is_active,
               DocumentationType.name)\
        .join(RepositoryOwner)\
        .join(RepositoryLang)\
        .outerjoin(Documentation)\
        .outerjoin(DocumentationType)\
        .all()

    return repo_details


def get_dest_dir(repo_name, repo_branch):
    return '{}/{}/{}'.format(config['REPO_LOCAL_BASEDIR'], repo_name, repo_branch)


def get_repo_source_dir(dest_dir, repo_url):
    real_repo_name = os.path.splitext(os.path.basename(repo_url))[0]
    return os.path.join(dest_dir, real_repo_name)


def clone_or_pull(repo_name, repo_url, repo_branch):
    dest_dir = get_dest_dir(repo_name, repo_branch)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        logger.info('Create local directory: {}'.format(dest_dir))

        args = ['git', 'clone', repo_url, '-b', repo_branch, '--single-branch']
        subprocess.check_output(args, cwd=dest_dir, stderr=subprocess.STDOUT)
        logger.info('Git clone repo [{}] to local dir: {}'.format(repo_name, dest_dir))

    args = ['git', 'pull']
    subprocess.check_output(args, cwd=get_repo_source_dir(dest_dir, repo_url), stderr=subprocess.STDOUT)
    logger.info('Git pull finished for repo: {}'.format(repo_name))


def run_doc_gen(doc_gen_script):
    with tempfile.TemporaryFile() as tmp:
        tmp.write(doc_gen_script)
        subprocess.call(tmp, stderr=subprocess.STDOUT)


def sync_worker(repo_name, repo_url, repo_branch, doc_gen_script):
    clone_or_pull(repo_name, repo_url, repo_branch)
    run_doc_gen(doc_gen_script)


def sync_repo_docs():
    repo_docs = get_active_repo_docs()
    jobs = []
    for repo, doc_gen_script in repo_docs.items():
        repo_name, repo_url, repo_branch = repo
        p = multiprocessing.Process(target=sync_worker, args=(repo_name, repo_url, repo_branch, doc_gen_script, ))
        p.start()
        jobs.append(p)

    for j in jobs:
        j.join()

    logger.info('All repos synced!')
