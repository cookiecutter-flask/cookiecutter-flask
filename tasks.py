#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import shutil

from invoke import task, run

HERE = os.path.abspath(os.path.dirname(__file__))
# Match default value of app_name from cookiecutter.json
COOKIE = os.path.join(HERE, 'myflaskapp')
REQUIREMENTS = os.path.join(COOKIE, 'requirements', 'dev.txt')


@task
def build():
    """Build the cookiecutter."""
    run('cookiecutter {0} --no-input'.format(HERE))


@task
def clean():
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')


def _run_manage_command(command):
    run('python {0} {1}'.format(os.path.join(COOKIE, 'manage.py'), command), echo=True)


@task(pre=[clean, build])
def test():
    """Run lint commands and tests."""
    run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS), echo=True)
    os.chdir(COOKIE)
    _run_manage_command('lint')
    _run_manage_command('test')
