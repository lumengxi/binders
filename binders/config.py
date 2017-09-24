import json
import os
from flask_appbuilder.security.manager import AUTH_DB

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder 
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = "Binders"

# Uncomment to setup Setup an App icon
APP_ICON = "/static/assets/images/binders.png"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"


# ---------------------------------------------------
# App config
# ---------------------------------------------------
PACKAGE_DIR = os.path.join(BASE_DIR, 'static', 'assets')
PACKAGE_FILE = os.path.join(PACKAGE_DIR, 'package.json')
with open(PACKAGE_FILE) as package_file:
    VERSION_STRING = json.load(package_file)['version']

# Theme configuration
APP_THEME = "yeti.css"

CELERY_RESULT_BACKEND = 'db+sqlite:///' + os.path.join(BASE_DIR, 'celery_results.db')
CELERY_BROKER_URL = 'sqla+sqlite:///' + os.path.join(BASE_DIR, 'celery.db')

REPO_LOCAL_BASEDIR = os.path.join(BASE_DIR, 'repos')


# ---------------------------------------------------
# Import local config
# ---------------------------------------------------
try:
    from local_config import *  # noqa
except:
    pass
