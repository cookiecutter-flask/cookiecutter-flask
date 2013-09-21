# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, session, request, flash, redirect, url_for
from .app import app, db
from .models import User
from .forms import RegisterForm, LoginForm
from .utils import flash_errors, login_required
from sqlalchemy.exc import IntegrityError


@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username'],
                                password=request.form['password']).first()
        if u is None:
            error = 'Invalid username or password.'
            flash(error, 'warning')
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
