# -*- coding: utf-8 -*-
import datetime as dt

from flask.ext.login import UserMixin

from {{cookiecutter.app_name}}.database import db, CRUDMixin
from {{cookiecutter.app_name}}.extensions import bcrypt


class User(UserMixin, CRUDMixin,  db.Model):

    __tablename__ = 'users'
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)  # The hashed password
    created_at = db.Column(db.DateTime(), nullable=False)
    active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean())

    def __init__(self, username=None, email=None, password=None,
                 active=False, is_admin=False):
        self.username = username
        self.email = email
        if password:
            self.set_password(password)
        self.active = active
        self.is_admin = is_admin
        self.created_at = dt.datetime.utcnow()

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return '<User "{username}">'.format(username=self.username)
