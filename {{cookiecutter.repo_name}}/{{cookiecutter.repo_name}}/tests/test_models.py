# -*- coding: utf-8 -*-
import unittest
from nose.tools import *  # PEP8 asserts
from flask.ext.testing import TestCase

from {{ cookiecutter.repo_name }}.app import create_app
from {{ cookiecutter.repo_name }}.models import User, db


class TestUser(TestCase):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

    def create_app(self):
        app = create_app(self, 'testing')
        with app.app_context():
            db.create_all()
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_check_password(self):
        user = User(username="foo", email="foo@bar.com",
                    password="foobarbaz123")
        db.session.add(user)
        db.session.commit()
        assert_true(user.check_password('foobarbaz123'))
        assert_false(user.check_password("barfoobaz"))

if __name__ == '__main__':
    unittest.main()
