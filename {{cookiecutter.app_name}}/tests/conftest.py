# -*- coding: utf-8 -*-
import os

import pytest

from {{ cookiecutter.app_name }}.settings import TestConfig
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.database import db as _db

from .factories import ALL_FACTORIES

@pytest.yield_fixture(scope='session')
def app():
    _app = create_app(TestConfig)
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.yield_fixture(scope='session')
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.drop_all()


@pytest.yield_fixture(scope='function')
def session(db):
    conn = db.engine.connect()
    transaction = conn.begin()

    opts = {'bind': conn, 'binds': {}}
    _session = db.create_scoped_session(options=opts)

    # Set session for each factory class
    for FactoryClass in ALL_FACTORIES:
        FactoryClass.FACTORY_SESSION = _session

    db.session = _session

    yield _session

    transaction.rollback()
    conn.close()
    _session.remove()
