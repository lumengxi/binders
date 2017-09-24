import logging
import os
from flask import Flask, redirect
from flask_appbuilder import SQLA, AppBuilder, IndexView
from flask_appbuilder.baseviews import expose
from flask_migrate import Migrate

APP_DIR = os.path.dirname(__file__)

# Logging configuration
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLA(app)

migrate = Migrate(app, db, directory=APP_DIR + "/migrations")


class MyIndexView(IndexView):
    @expose('/')
    def index(self):
        return redirect('/binders/welcome')

appbuilder = AppBuilder(
    app=app,
    session=db.session,
    base_template='binders/base.html',
    indexview=MyIndexView
)

from binders import views  # noqa
