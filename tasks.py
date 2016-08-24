#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import json
import shutil

from invoke import task, run

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of app_name from cookiecutter.json
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS['app_name'])
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
    run('FLASK_APP="{0}.autoapp" flask {1}'.format(COOKIECUTTER_SETTINGS['app_name'], command), echo=True)


@task(pre=[clean, build])
def test():
    """Run lint commands and tests."""
    run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS), echo=True)
    os.chdir(COOKIE)
    run('pwd', echo=True)
    #_run_manage_command('lint')
    _run_manage_command('test')
