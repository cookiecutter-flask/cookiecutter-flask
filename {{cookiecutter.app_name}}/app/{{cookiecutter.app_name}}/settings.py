# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('APP_SECRET', 'fakeSecretKey')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEBPACK_MANIFEST_PATH = os.path.join(APP_DIR, 'webpack/manifest.json')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{passwd}@/{db_name}?host={host}'.format(
        user=os.environ.get('POSTGRES_USER', 'fakePostgresUser'),
        passwd=os.environ.get('POSTGRES_PASSWORD', 'fakePassword'),
        db_name=os.environ.get('POSTGRES_DB', 'fakeDB'),
        host=os.environ.get('POSTGRES_HOST', 'fakeDbHost')
    )


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    # Put the db file in project root
    DEBUG_TB_ENABLED = True
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
