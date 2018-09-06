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
REQUIREMENTS = os.path.join(COOKIE, 'requirements', 'dev.txt')


def _run_npm_command(ctx, command):
    os.chdir(COOKIE)
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
    os.chdir(COOKIE)
    ctx.run('flask {0}'.format(command), echo=True)


@task(pre=[clean, build])
def test(ctx):
    """Run lint commands and tests."""
    ctx.run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS),
            echo=True)
    _run_npm_command(ctx, 'run lint')
    os.chdir(COOKIE)
    shutil.copyfile(os.path.join(COOKIE, '.env.example'),
                    os.path.join(COOKIE, '.env'))
    _run_flask_command(ctx, 'lint')
    _run_flask_command(ctx, 'test')


@task
def readme(ctx, browse=False):
    ctx.run('rst2html.py README.rst > README.html')
    if browse:
        webbrowser.open_new_tab('README.html')
