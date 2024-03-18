"""Invoke tasks."""
import os
import shutil
from typing import Iterator

# isort: off
# Temporary monkeypatch; see https://github.com/pyinvoke/invoke/issues/833
import inspect

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

from invoke import task

# isort: on

HERE = os.path.abspath(os.path.dirname(__file__))
DEFAULT_APP_NAME = "my_flask_app"
COOKIE = os.path.join(HERE, DEFAULT_APP_NAME)
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
    ctx.run(f"python cookiecutter_spec.py {HERE} --no-input")


@task(pre=[build])
def build_install(ctx):
    """Build the cookiecutter."""
    _run_npm_command(ctx, "install")
    ctx.run(f"pip install -r {REQUIREMENTS} --ignore-installed", echo=True)


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)


@task(pre=[clean, build_install])
def lint(ctx):
    """Run lint commands."""
    _run_npm_command(ctx, "run lint")
    os.chdir(COOKIE)
    os.environ["FLASK_ENV"] = "production"
    os.environ["FLASK_DEBUG"] = "0"
    _run_flask_command(ctx, "lint", "--check")


@task(pre=[clean, build_install])
def test(ctx):
    """Run tests."""
    os.chdir(COOKIE)
    os.environ["FLASK_ENV"] = "production"
    os.environ["FLASK_DEBUG"] = "0"
    _run_flask_command(ctx, "test")


def _walk_template_files() -> Iterator[str]:
    template_dir = os.path.join(HERE, "{{cookiecutter.app_name}}")
    for root, _, template_files in os.walk(template_dir):
        for template_file in template_files:
            yield os.path.join(root, template_file)


@task
def no_placeholders(ctx):
    """Check that default project name hasn't been committed to template dir"""
    for template_file in _walk_template_files():
        try:
            with open(template_file, "r") as f:
                if DEFAULT_APP_NAME in f.read():
                    raise ValueError(
                        f"Template cannot contain default app name, but {DEFAULT_APP_NAME} found in {f.name}"
                    )
        except UnicodeDecodeError:
            pass


@task(pre=[clean, build])
def test_image_build(ctx):
    """Run tests."""
    os.chdir(COOKIE)
    os.environ["DOCKER_BUILDKIT"] = "1"
    ctx.run("docker compose build flask-dev", echo=True)
