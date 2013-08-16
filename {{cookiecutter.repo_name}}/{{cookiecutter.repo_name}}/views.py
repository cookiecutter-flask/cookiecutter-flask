# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, session, request, flash, redirect, url_for
from functools import wraps
from .app import app, db
from .models import User
from .forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the {0} field - {1}"
                    .format(getattr(form, field).label.text, error), 'error')

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('home'))
    return wrap

@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username'],
                                password=request.form['password']).first()
        if u is None:
            error = 'Invalid username or password.'
            flash(error, 'error')
        else:
            session['logged_in'] = True
            session['username'] = u.username
            flash("You are logged in.", 'success')
            return redirect(url_for("members"))
    return render_template("home.html", form=form)


@app.route("/members/")
@login_required
def members():
    return render_template("members.html")


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You are logged out.', 'info')
    return redirect(url_for('home'))

@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User(form.username.data, form.email.data, form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Thank you for registering. You can now log in.", 'success')
            return redirect(url_for('home'))
        except IntegrityError as err:
            print(err)
            flash("That username and/or email already exists. Try again.", 'error')
    else:
        flash_errors(form)
    return render_template('register.html', form=form)


@app.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("about.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
