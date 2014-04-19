#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.user.models import User
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig
from {{cookiecutter.app_name}}.database import db

if os.environ.get("{{cookiecutter.app_name | upper}}_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)
TEST_CMD = "py.test tests"

def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User}

@manager.command
def test():
    """Run the tests."""
    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)

manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
