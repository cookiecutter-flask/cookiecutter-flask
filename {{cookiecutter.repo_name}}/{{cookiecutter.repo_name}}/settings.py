# -*- coding: utf-8 -*-
import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
DB_NAME = "test.db"
DB_PATH = os.path.join(PROJECT_ROOT, DB_NAME)
SQLALCHEMY_DATABASE_URI = "sqlite:///{0}".format(DB_PATH)
DEBUG = True
SECRET_KEY = 'shhhh'
