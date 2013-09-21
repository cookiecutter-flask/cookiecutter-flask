#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point for all things, to avoid circular imports.
"""
import os
from .app import app, db, assets_env
from .models import *
from .views import *


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
