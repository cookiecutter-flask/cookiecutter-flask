# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related
utilities.
"""
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator

from .extensions import db, bcrypt

Column = db.Column
relationship = relationship

class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        if any(
            (isinstance(id, basestring) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

# From Mike Bayer's "atmcraft" example app
# https://speakerdeck.com/zzzeek/building-the-app
def ReferenceCol(tablename, nullable=False, **kwargs):
    """Column that adds primary key foreign key reference."""
    return db.Column(
        db.ForeignKey("{0}.id".format(tablename)),
        nullable=nullable, **kwargs)


class Password(str):
    """Coerce a string to a bcrypt password.

    Rationale: for an easy string comparison,
    so we can say ``some_password == 'hello123'``

    .. seealso::

        https://pypi.python.org/pypi/bcrypt/

    """

    def __new__(cls, value, crypt=True):
        if value is None:
            return None
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        if crypt:
            value = bcrypt.generate_password_hash(value)
        return str.__new__(cls, value)

    def __eq__(self, other):
        if other and not isinstance(other, Password):
            return bcrypt.check_password_hash(self, other)
        return str.__eq__(self, other)

    def __ne__(self, other):
        if other and not isinstance(other, Password):
            return bcrypt.check_password_hash(self, other)
        return not self.__eq__(other)


class BcryptType(TypeDecorator):
    """Coerce strings to bcrypted Password objects for the database.
    """
    impl = db.String(128)

    def process_bind_param(self, value, dialect):
        return Password(value)

    def process_result_value(self, value, dialect):
        # already crypted, so don't crypt again
        return Password(value, crypt=False)

    def __repr__(self):
        return "BcryptType()"
