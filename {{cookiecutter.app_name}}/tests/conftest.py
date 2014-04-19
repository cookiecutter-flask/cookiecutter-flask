# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import os

import pytest
from webtest import TestApp

from {{ cookiecutter.app_name }}.settings import TestConfig
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.database import db as _db


@pytest.yield_fixture(scope='session')
def app():
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture(scope='session')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)

@pytest.yield_fixture(scope='function')
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.drop_all()
