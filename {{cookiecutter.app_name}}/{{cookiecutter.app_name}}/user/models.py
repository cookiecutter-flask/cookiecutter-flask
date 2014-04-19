# -*- coding: utf-8 -*-
import datetime as dt

from flask.ext.login import UserMixin

from {{cookiecutter.app_name}}.database import (
    db,
    CRUDMixin,
    ReferenceCol,
    relationship,
    Column,
    BcryptType,
)


class Role(CRUDMixin, db.Model):
    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = ReferenceCol('users', nullable=True)
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)

class User(UserMixin, CRUDMixin,  db.Model):

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(BcryptType, nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, username, email, **kwargs):
        db.Model.__init__(self, username=username, email=email, **kwargs)

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __repr__(self):
        return '<User {username!r}>'.format(username=self.username)
