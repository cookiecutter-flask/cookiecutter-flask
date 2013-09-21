#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server
from {{ cookiecutter.repo_name }} import models
from {{ cookiecutter.repo_name }}.main import app, db

manager = Manager(app)

def _make_context():
    '''Return context dict for a shell session so you can access
    app, db, and models by default.
    '''
    return {'app': app, 'db': db, 'models': models}

@manager.command
def createdb():
    '''Create a database from the tables defined in models.py.'''
    db.create_all()

manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
