# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader

from {{cookiecutter.repo_name}} import assets

app = Flask(__name__)
# The environment variable, either 'prod' or 'dev'
env = os.environ.get("{{cookiecutter.repo_name | upper}}_ENV", "prod")
# Use the appropriate environment-specific settings
app.config.from_object('{{cookiecutter.repo_name}}.settings.{env}Config'
                        .format(env=env.capitalize()))
app.config['ENV'] = env
db = SQLAlchemy(app)

# Register asset bundles
assets_env = Environment()
assets_env.init_app(app)
assets_loader = PythonLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)
