# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_login import LoginManager
login_manager = LoginManager()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = Migrate()

from flask_cache import Cache
cache = Cache()

from flask_debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()
