# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader

from {{ cookiecutter.repo_name }}.settings import ProdConfig
from {{cookiecutter.repo_name}} import assets
from {{cookiecutter.repo_name}}.database import db
from {{cookiecutter.repo_name}} import public, user

assets_env = Environment()

def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    # Initialize SQLAlchemy
    db.init_app(app)
    # Register asset bundles
    assets_env.init_app(app)
    assets_loader = PythonLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)
    register_blueprints(app)
    return app


def register_blueprints(app):
    # Register blueprints
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    return app
