# -*- coding: utf-8 -*-
"""Reminder UI views."""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app.forms import ReminderForm
from app.models import Reminder
from app.extensions import db
from app.utils import flash_errors

blueprint = Blueprint("reminders", __name__, url_prefix="/reminders")


@blueprint.route("/")
@login_required
def list():
    """List user's reminders."""
    reminders = Reminder.query.filter_by(user_id=current_user.id).order_by(Reminder.due_date).all()
    return render_template("reminders/list.html", reminders=reminders)


@blueprint.route("/new", methods=["GET", "POST"])
@login_required
def new():
    """Create a new reminder."""
    form = ReminderForm(request.form)
    if form.validate_on_submit():
        reminder = Reminder.create(
            title=form.title.data,
            content=form.content.data,
            due_date=form.due_date.data,
            user_id=current_user.id,
        )
        flash(f"Reminder '{reminder.title}' created successfully.", "success")
        return redirect(url_for("reminders.list"))
    else:
        flash_errors(form)
    return render_template("reminders/form.html", form=form, title="New Reminder")


@blueprint.route("/<int:reminder_id>/edit", methods=["GET", "POST"])
@login_required
def edit(reminder_id):
    """Edit a reminder."""
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first_or_404()
    form = ReminderForm(request.form, obj=reminder)
    
    if form.validate_on_submit():
        form.populate_obj(reminder)
        db.session.commit()
        flash(f"Reminder '{reminder.title}' updated successfully.", "success")
        return redirect(url_for("reminders.list"))
    else:
        flash_errors(form)
    
    return render_template("reminders/form.html", form=form, title="Edit Reminder", reminder=reminder)


@blueprint.route("/<int:reminder_id>/complete", methods=["POST"])
@login_required
def complete(reminder_id):
    """Mark a reminder as complete."""
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first_or_404()
    reminder.completed = True
    db.session.commit()
    flash(f"Reminder '{reminder.title}' marked as complete.", "success")
    return redirect(url_for("reminders.list"))


@blueprint.route("/<int:reminder_id>/delete", methods=["POST"])
@login_required
def delete(reminder_id):
    """Delete a reminder."""
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first_or_404()
    title = reminder.title
    db.session.delete(reminder)
    db.session.commit()
    flash(f"Reminder '{title}' deleted successfully.", "info")
    return redirect(url_for("reminders.list"))
