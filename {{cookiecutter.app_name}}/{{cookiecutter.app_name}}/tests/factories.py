# -*- coding: utf-8 -*-
from factory import Sequence, PostGenerationMethodCall
from factory.alchemy import SQLAlchemyModelFactory

from {{cookiecutter.app_name}}.user.models import User
from {{cookiecutter.app_name}}.database import db


class UserFactory(SQLAlchemyModelFactory):
    FACTORY_SESSION = db.session
    FACTORY_FOR = User

    username = Sequence(lambda n: "user{0}".format(n))
    email = Sequence(lambda n: "user{0}@example.com".format(n))
    password = PostGenerationMethodCall("set_password", 'example')
    active = True
