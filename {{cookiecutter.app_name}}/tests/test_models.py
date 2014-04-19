# -*- coding: utf-8 -*-
import unittest
import datetime as dt

import pytest

from {{ cookiecutter.app_name }}.database import db
from {{ cookiecutter.app_name }}.user.models import User, Role
from .base import DbTestCase
from .factories import UserFactory


def test_created_at_defaults_to_datetime(session):
    user = User(username='foo', email='foo@bar.com')
    user.save()
    assert bool(user.created_at)
    assert isinstance(user.created_at, dt.datetime) is True

def test_password_is_nullable(session):
    user = User(username='foo', email='foo@bar.com')
    user.save()
    assert user.password is None

def test_factory(session):
    user = UserFactory(password="myprecious")
    assert bool(user.username)
    assert bool(user.email)
    assert bool(user.created_at)
    assert user.is_admin is False
    assert user.active is True
    assert user.password == "myprecious"

def test_check_password_with_equality_operators(session):
    user = User.create(username="foo", email="foo@bar.com",
                password="foobarbaz123")
    assert user.password == 'foobarbaz123'
    assert user.password != "barfoobaz"

def test_full_name(session):
    user = UserFactory(first_name="Foo", last_name="Bar")
    assert user.full_name == "Foo Bar"

def test_roles(session):
    role = Role(name='admin')
    role.save()
    u = UserFactory()
    u.roles.append(role)
    u.save()
    assert role in u.roles

if __name__ == '__main__':
    unittest.main()
