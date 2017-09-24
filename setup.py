import os
import subprocess
import json
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DIR = os.path.join(BASE_DIR, 'binders', 'static', 'assets')

VERSION_STRING = '0.1.0'


def get_git_sha():
    try:
        return str(subprocess.check_output(['git', 'rev-parse', 'HEAD'])).strip()
    except:
        return ""


GIT_SHA = get_git_sha()
version_info = {
    'version': VERSION_STRING,
    'git_sha': GIT_SHA,
}
print("-==-" * 15)
print("VERSION: " + VERSION_STRING)
print("GIT SHA: " + GIT_SHA)
print("-==-" * 15)

with open(os.path.join(PACKAGE_DIR, 'version_info.json'), 'w') as version_file:
    json.dump(version_info, version_file)


setup(
    name='binders',
    description='Service/library documentation registry',
    version=VERSION_STRING,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=['binders/bin/binders'],
    install_requires=[
        'colorama==0.3.9',
        'cryptography==1.7.2',
        'flask-appbuilder==1.9.4',
        'flask-cache==0.13.1',
        'flask-migrate==2.1.1',
        'flask-script==2.0.5',
        'flask-sqlalchemy==2.1',
        'flask-testing==0.6.2',
        'flask-wtf==0.14.2',
        'gunicorn==19.7.1',
        'python-dateutil==2.6.1',
        'sqlalchemy==1.1.14',
        'sqlalchemy-utils==0.32.14',
        'psycopg2',
    ],
    extras_require={
        'cors': ['Flask-Cors>=2.0.0'],
    },
    tests_require=[
        'codeclimate-test-reporter',
        'coverage',
        'mock',
        'pytest',
        'flake8',
        'pylint',
        'pylama'
    ],
    author='Mengxi Lu',
    url='https://github.com/lumengxi/binders',
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)