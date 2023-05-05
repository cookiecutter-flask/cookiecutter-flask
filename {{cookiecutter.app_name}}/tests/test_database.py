# -*- coding: utf-8 -*-
"""Database unit tests."""
import pytest
from flask_login import UserMixin
from sqlalchemy import text
from sqlalchemy.orm.exc import ObjectDeletedError

from {{cookiecutter.app_name}}.database import Column, PkModel, db


class ExampleUserModel(UserMixin, PkModel):
    """Example model class for a user."""

    __tablename__ = "testusers"
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, username, email):
        """Create instance."""
        super().__init__(username=username, email=email)


@pytest.mark.usefixtures("db")
class TestCRUDMixin:
    """CRUDMixin tests."""

    def test_create(self):
        """Test CRUD create."""
        user = ExampleUserModel.create(username="foo", email="foo@bar.com")
        assert ExampleUserModel.get_by_id(user.id).username == "foo"

    def test_create_save(self):
        """Test CRUD create with save."""
        user = ExampleUserModel("foo", "foo@bar.com")
        user.save()
        assert ExampleUserModel.get_by_id(user.id) is not None

    def test_delete_with_commit(self):
        """Test CRUD delete with commit."""
        user = ExampleUserModel("foo", "foo@bar.com")
        user.save()
        user.delete(commit=True)
        assert ExampleUserModel.get_by_id(user.id) is None

    def test_delete_without_commit_cannot_access(self):
        """Test CRUD delete without commit."""
        user = ExampleUserModel("foo", "foo@bar.com")
        user.save()
        user.delete(commit=False)
        with pytest.raises(ObjectDeletedError):
            ExampleUserModel.get_by_id(user.id)

    @pytest.mark.parametrize("commit,expected", [(True, "bar"), (False, "foo")])
    def test_update(self, commit, expected, db):
        """Test CRUD update with and without commit."""
        user = ExampleUserModel(username="foo", email="foo@bar.com")
        user.save()
        user.update(commit=commit, username="bar")
        query = text("select * from testusers")
        retrieved = db.session.execute(query).fetchone()
        assert retrieved.username == expected


class TestPkModel:
    """PkModel tests."""

    def test_get_by_id_wrong_type(self):
        """Test get_by_id returns None for non-numeric argument."""
        assert ExampleUserModel.get_by_id("xyz") is None
