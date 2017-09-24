import logging
from binders import db
from binders.models.core import DocumentationType


CREATED_BY = 'prefill'


def fill_document_type():
    try:
        for t in ['swagger', 'javac', 'sphinx']:
            db.session.add(DocumentationType(name=t))
        db.session.commit()
        logging.info('Prefilled document_type table')
    except Exception as e:
        logging.error('Cannot prefill document_type: {}'.format(e))
        db.session.rollback()


def fill_repo_lang():
    try:
        for t in ['java', 'python', 'clojure']:
            db.session.add(DocumentationType(name=t))
        db.session.commit()
        logging.info('Prefilled repository_lang table')
    except Exception as e:
        logging.error('Cannot prefill repository_lang: {}'.format(e))
        db.session.rollback()
