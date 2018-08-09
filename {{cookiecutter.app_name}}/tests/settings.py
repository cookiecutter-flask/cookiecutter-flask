"""Settings module for test app."""
ENV = 'development'
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite://'
SECRET_KEY = 'not-so-secret-in-tests'
BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
DEBUG_TB_ENABLED = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
WTF_CSRF_ENABLED = False  # Allows form testing
