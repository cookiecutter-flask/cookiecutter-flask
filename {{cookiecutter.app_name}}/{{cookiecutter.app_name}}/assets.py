# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle, Environment

css = Bundle(
    "libs/bootstrap3/css/bootstrap.min.css",
    "css/style.css",
    filters="cssmin",
    output="public/css/common.css"
)

js = Bundle(
    "libs/jquery2/jquery-2.0.3.min.js",
    "libs/bootstrap3/js/bootstrap.min.js",
    "js/plugins.js",
    Bundle(
        "js/script.js",
        filters="jsmin"
    ),
    output="public/js/common.js"
)

assets = Environment()

assets.register("js_all", js)
assets.register("css_all", css)
