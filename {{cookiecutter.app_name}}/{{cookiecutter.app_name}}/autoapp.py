# -*- coding: utf-8 -*-
"""Create an application instance."""
import os

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig

CONFIG = ProdConfig if os.environ.get('{{cookiecutter.app_name | upper}}_ENV') == 'prod' else DevConfig

app = create_app(CONFIG)
