"""Invoke tasks."""
import json
import os
import shutil

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "cookiecutter.json"), "r") as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of app_name from cookiecutter.json
COOKIECUTTER_SETTINGS["app_name"] = "my_flask_app"
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS["app_name"])
REQUIREMENTS = os.path.join(COOKIE, "requirements", "dev.txt")


def _run_npm_command(ctx, command):
    os.chdir(COOKIE)
    ctx.run(f"npm {command}", echo=True)
    os.chdir(HERE)


def _run_flask_command(ctx, command, *args):
    os.chdir(COOKIE)
    flask_command = f"flask {command}"
    if args:
        flask_command += f" {' '.join(args)}"
    ctx.run(flask_command, echo=True)


@task
def build(ctx):
    """Build the cookiecutter."""
    ctx.run(f"cookiecutter {HERE} --no-input")
    _run_npm_command(ctx, "install")
    ctx.run(f"pip install -r {REQUIREMENTS} --ignore-installed", echo=True)


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)


@task(pre=[clean, build])
def lint(ctx):
    """Run lint commands."""
    _run_npm_command(ctx, "run lint")
    os.chdir(COOKIE)
    os.environ["FLASK_ENV"] = "production"
    os.environ["FLASK_DEBUG"] = "0"
    _run_flask_command(ctx, "lint", "--check")


@task(pre=[clean, build])
def test(ctx):
    """Run tests."""
    os.chdir(COOKIE)
    os.environ["FLASK_ENV"] = "production"
    os.environ["FLASK_DEBUG"] = "0"
    _run_flask_command(ctx, "test")
