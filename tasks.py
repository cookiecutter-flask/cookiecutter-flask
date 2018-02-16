#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import json
import shutil
import webbrowser

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of app_name from cookiecutter.json
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS['app_name'])
COOKIE_APP = os.path.join(HERE, COOKIECUTTER_SETTINGS['app_name'], 'app')
AUTOAPP = os.path.join(COOKIE_APP, 'autoapp.py')
REQUIREMENTS = os.path.join(COOKIE_APP, 'requirements', 'dev.txt')

os.environ['FLASK_DEBUG'] = '1'


def _run_npm_command(ctx, command):
    os.chdir(COOKIE_APP)
    ctx.run('npm {0}'.format(command), echo=True)
    os.chdir(HERE)


@task
def build(ctx):
    """Build the cookiecutter."""
    ctx.run('cookiecutter {0} --no-input'.format(HERE))
    _run_npm_command(ctx, 'install')
    _run_npm_command(ctx, 'run build')


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')


def _run_flask_command(ctx, command):
    ctx.run('FLASK_APP={0} flask {1}'.format(AUTOAPP, command), echo=True)


@task(pre=[clean, build])
def test(ctx):
    """Run lint commands and tests."""
    ctx.run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS),
            echo=True)
    _run_npm_command(ctx, 'run lint')
    os.chdir(COOKIE_APP)
    _run_flask_command(ctx, 'lint')
    _run_flask_command(ctx, 'test')

@task
def readme(ctx, browse=False):
    ctx.run("rst2html.py README.rst > README.html")
    if browse:
        webbrowser.open_new_tab('README.html')
