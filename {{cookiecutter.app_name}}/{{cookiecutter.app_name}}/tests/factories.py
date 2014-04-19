# -*- coding: utf-8 -*-
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from myflaskapp.user.models import User
from myflaskapp.database import db

class BaseFactory(SQLAlchemyModelFactory):

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        """Create an instance of the model, and save it to the database."""
        session = cls.FACTORY_SESSION
        obj = target_class(*args, **kwargs)
        session.add(obj)
        session.commit()
        return obj


class UserFactory(BaseFactory):
    FACTORY_SESSION = db.session
    FACTORY_FOR = User

    username = Sequence(lambda n: "user{0}".format(n))
    email = Sequence(lambda n: "user{0}@example.com".format(n))
    password = 'example'
    active = True
