# -*- coding: utf-8 -*-
"""Application models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from app.database import Column, PkModel, db, reference_col, relationship
from app.extensions import bcrypt


class Role(PkModel):
    """A role for a user."""

    __tablename__ = "roles"
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Role({self.name})>"


class User(UserMixin, PkModel):
    """A user of the app."""

    __tablename__ = "users"
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    _password = Column("password", db.LargeBinary(128), nullable=True)
    created_at = Column(
        db.DateTime, nullable=False, default=dt.datetime.now(dt.timezone.utc)
    )
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self._password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"


# Reminder models for future functionality
class Reminder(PkModel):
    """A reminder for a user."""

    __tablename__ = "reminders"
    title = Column(db.String(200), nullable=False)
    content = Column(db.Text, nullable=True)
    due_date = Column(db.DateTime, nullable=False)
    created_at = Column(
        db.DateTime, nullable=False, default=dt.datetime.now(dt.timezone.utc)
    )
    completed = Column(db.Boolean(), default=False)
    user_id = reference_col("users", nullable=False)
    user = relationship("User", backref="reminders")

    def __init__(self, title, due_date, user_id, **kwargs):
        """Create instance."""
        super().__init__(title=title, due_date=due_date, user_id=user_id, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Reminder({self.title!r})>"

    @property
    def is_overdue(self):
        """Check if reminder is overdue."""
        return not self.completed and self.due_date < dt.datetime.now(dt.timezone.utc)
