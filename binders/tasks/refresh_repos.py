import os

from binders import app
from binders.tasks import get_celery_app

config = app.config
celery_app = get_celery_app(config)


@celery_app.task()
def refresh_repo():
    repo_dir = config['REPO_LOCAL_DIR']

