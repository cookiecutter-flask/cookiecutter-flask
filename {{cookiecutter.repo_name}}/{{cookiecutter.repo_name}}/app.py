# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.assets import Environment
from flask_debugtoolbar import DebugToolbarExtension
from webassets.loaders import PythonLoader

from {{cookiecutter.repo_name}}.settings import ProdConfig
from {{cookiecutter.repo_name}}.assets import assets
from {{cookiecutter.repo_name}}.extensions import db, login_manager
from {{cookiecutter.repo_name}} import public, user


def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    assets.init_app(app)
    toolbar = DebugToolbarExtension(app)
    return None


def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    return None
