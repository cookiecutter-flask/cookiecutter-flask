# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# The environment variable, either 'prod' or 'dev'
env = os.environ.get("{{cookiecutter.repo_name | upper}}_ENV", "prod")
# Use the appropriate environment-specific settings
app.config.from_object('{{cookiecutter.repo_name}}.settings.{env}Config'
                        .format(env=env.capitalize()))
app.config['ENV'] = env
db = SQLAlchemy(app)
