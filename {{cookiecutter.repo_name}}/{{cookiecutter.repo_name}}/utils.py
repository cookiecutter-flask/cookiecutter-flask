# -*- coding: utf-8 -*-
'''Helper utilities and decorators.'''
from flask import session, flash, redirect, url_for
from functools import wraps

def flash_errors(form):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the {0} field - {1}"
                    .format(getattr(form, field).label.text, error), 'warning')

def login_required(test):
    '''Decorator that makes a view require authentication.'''
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('home'))
    return wrap
