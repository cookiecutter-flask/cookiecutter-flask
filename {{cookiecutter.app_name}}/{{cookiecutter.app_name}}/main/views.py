# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from flask_admin import BaseView, expose, AdminIndexView
from flask_admin .contrib.sqla import ModelView

blueprint = Blueprint('main', __name__, url_prefix='/main', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('main/members.html')


class AdminAccessControlMixin(object):
    """Configure general admin access authorization details here.
    Make sure this class goes first in the parent list of model classes.
    """

    @staticmethod
    def is_accessible():
        return current_user.is_authenticated and current_user.username == 'admin'


class UserModelView(AdminAccessControlMixin, ModelView):
    pass


class SiteConfigView(AdminAccessControlMixin, BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/site_config.html')


class LoginFriendlyAdminIndexView(AdminIndexView):
    """We add the automated redirection to login on the home page of this view for convenience."""

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('public.home', next=url_for('admin.index')))
        return super(LoginFriendlyAdminIndexView, self).index()
