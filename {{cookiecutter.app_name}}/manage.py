#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Management script."""
import os
from glob import glob
from subprocess import call

from flask_migrate import MigrateCommand
from flask_script import Command, Manager, Option, Server, Shell
from flask_script.commands import Clean, ShowUrls

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.database import db
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig
from {{cookiecutter.app_name}}.user.models import User

if os.environ.get('{{cookiecutter.app_name | upper}}_ENV') == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access app, db, and the User model by default."""
    return {'app': app, 'db': db, 'User': User}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


class Lint(Command):
    """Lint and check code style."""

    def get_options(self):
        """Command line options."""
        return (
            Option('-f', '--fix',
                   action='store_true',
                   dest='fix_imports',
                   default=False,
                   help='Fix imports before linting'),
        )

    def run(self, fix_imports):
        """Run command."""
        skip = ['requirements']
        root_files = glob('*.py')
        root_directories = [name for name in next(os.walk('.'))[1] if not name.startswith('.')]
        arguments = [arg for arg in root_files + root_directories if arg not in skip]

        if fix_imports:
            command_line = ['isort', '-rc'] + arguments
            print('Fixing import order: %s' % ' '.join(command_line))
            call(command_line)

        command_line = ['flake8'] + arguments
        print('Checking code style: %s' % ' '.join(command_line))
        exit(call(command_line))


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('lint', Lint())

if __name__ == '__main__':
    manager.run()
