# -*- coding: utf-8 -*-
"""Database unit tests."""
import pytest
from flask_login import UserMixin

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

    def test_delete_with_commit(self):
        """Test CRUD delete with commit."""
        user = ExampleUserModel("foo", "foo@bar.com")
        user.save()
        assert ExampleUserModel.get_by_id(user.id) is not None
        user.delete(commit=True)
        assert ExampleUserModel.get_by_id(user.id) is None

    def test_delete_without_commit(self):
        """Test CRUD delete without commit."""
        user = ExampleUserModel("foo", "foo@bar.com")
        user.save()
        user.delete(commit=False)
        assert ExampleUserModel.get_by_id(user.id) is not None

    @pytest.mark.parametrize("commit,expected", [(True, "bar"), (False, "foo")])
    def test_update(self, commit, expected, db):
        """Test CRUD update with and without commit."""
        user = ExampleUserModel(username="foo", email="foo@bar.com")
        user.save()
        user.update(commit=commit, username="bar")
        retrieved = db.session.execute("""select * from testusers""").fetchone()
        assert retrieved.username == expected


class TestPkModel:
    """PkModel tests."""

    def test_get_by_id_wrong_type(self):
        """Test get_by_id returns None for non-numeric argument."""
        assert ExampleUserModel.get_by_id("xyz") is None
