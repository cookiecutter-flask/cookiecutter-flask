# -*- coding: utf-8 -*-
from passlib.apps import custom_app_context as pwd_context
from {{cookiecutter.repo_name}}.database import db


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def check_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '<User "{username}">'.format(username=self.username)
