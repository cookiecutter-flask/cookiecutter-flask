# -*- coding: utf-8 -*-
'''Members-only module, typically including the app itself.
'''
from flask import Blueprint, render_template
from {{cookiecutter.repo_name}}.utils import login_required

blueprint = Blueprint('member', __name__,
                        static_folder="../static",
                        template_folder="../templates")

@blueprint.route("/members/")
@login_required
def members():
    return render_template("members.html")
