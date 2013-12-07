# -*- coding: utf-8 -*-
import unittest
from nose.tools import *  # PEP8 asserts
from flask.ext.testing import TestCase

from {{ cookiecutter.repo_name }}.app import create_app
from {{ cookiecutter.repo_name }}.database import db
from {{ cookiecutter.repo_name }}.user.models import User
from .factories import UserFactory


class TestUser(TestCase):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

    def create_app(self):
        app = create_app(self)
        with app.app_context():
            db.create_all()
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_factory(self):
        user = UserFactory(password="myprecious")
        assert_true(user.username)
        assert_true(user.email)
        assert_true(user.created_at)
        assert_false(user.is_admin)
        assert_false(user.active)
        assert_true(user.check_password("myprecious"))

    def test_check_password(self):
        user = User(username="foo", email="foo@bar.com",
                    password="foobarbaz123")
        db.session.add(user)
        db.session.commit()
        assert_true(user.check_password('foobarbaz123'))
        assert_false(user.check_password("barfoobaz"))

if __name__ == '__main__':
    unittest.main()
