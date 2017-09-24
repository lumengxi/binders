from celery import Celery

from binders import app

_celery_app = None


def get_celery_app(config):
    global _celery_app
    if _celery_app:
        return _celery_app

    _celery_app = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'])

    _celery_app.conf.update(app.config)

    class ContextTask(_celery_app.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return _celery_app.Task.__call__(self, *args, **kwargs)

    _celery_app.Task = ContextTask

    return _celery_app
