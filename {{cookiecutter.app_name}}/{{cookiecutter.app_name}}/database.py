# -*- coding: utf-8 -*-
'''Database module, including the SQLAlchemy database object and DB-related
utilities.
'''

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from .extensions import db

# Helpers from Mike Bayer's atmcraft example app
# https://bitbucket.org/zzzeek/pycon2014_atmcraft/src/a6d96575bc49?at=master
def many_to_one(clsname, **kw):
    """Use an event to build a many-to-one relationship on a class.

    This makes use of the :meth:`.References._reference_table` method
    to generate a full foreign key relationship to the remote table.

    """
    @declared_attr
    def m2o(cls):
        cls._references((cls.__name__, clsname))
        return relationship(clsname, **kw)
    return m2o

def one_to_many(clsname, **kw):
    """Use an event to build a one-to-many relationship on a class.

    This makes use of the :meth:`.References._reference_table` method
    to generate a full foreign key relationship from the remote table.

    """
    @declared_attr
    def o2m(cls):
        cls._references((clsname, cls.__name__))
        return relationship(clsname, **kw)
    return o2m


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
        '''Create a new record and save it the database.'''
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        '''Update specific fields of a record.'''
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        '''Save the record.'''
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        '''Remove the record from the database.'''
        db.session.delete(self)
        return commit and db.session.commit()
