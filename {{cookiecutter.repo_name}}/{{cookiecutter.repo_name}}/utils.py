# -*- coding: utf-8 -*-
'''Helper utilities and decorators.'''
from flask import flash

def flash_errors(form):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in {0} field - {1}"
                    .format(getattr(form, field).label.text, error), 'warning')
