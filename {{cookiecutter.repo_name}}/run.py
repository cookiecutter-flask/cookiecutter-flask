#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from {{cookiecutter.repo_name}} import main

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    main.app.run(port=port)
