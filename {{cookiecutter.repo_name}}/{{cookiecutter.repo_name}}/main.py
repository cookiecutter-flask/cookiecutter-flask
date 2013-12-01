#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point for all things, to avoid circular imports.
"""
import os
from .app import create_app
from .models import User, db
import {{cookiecutter.repo_name}}.modules as modules

if __name__ == '__main__':
    # Get the environment setting from the system environment variable
    env = os.environ.get("{{cookiecutter.repo_name | upper}}_ENV", "prod")
    app = create_app("{{cookiecutter.repo_name}}.settings.{env}Config"
                        .format(env=env.capitalize()))
