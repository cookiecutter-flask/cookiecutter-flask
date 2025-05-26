# -*- coding: utf-8 -*-
"""API endpoints for reminders."""
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from werkzeug.exceptions import BadRequest, NotFound

from app.forms import ReminderForm
from app.models import Reminder
from app.extensions import db

blueprint = Blueprint("api_reminders", __name__, url_prefix="/api/reminders")


@blueprint.route("/", methods=["GET"])
@login_required
def list_reminders():
    """List user's reminders via API."""
    reminders = Reminder.query.filter_by(user_id=current_user.id).order_by(Reminder.due_date).all()
    
    return jsonify({
        "reminders": [
            {
                "id": reminder.id,
                "title": reminder.title,
                "content": reminder.content,
                "due_date": reminder.due_date.isoformat(),
                "created_at": reminder.created_at.isoformat(),
                "completed": reminder.completed,
                "is_overdue": reminder.is_overdue
            }
            for reminder in reminders
        ]
    }), 200


@blueprint.route("/", methods=["POST"])
@login_required
def create_reminder():
    """Create a new reminder via API."""
    if not request.is_json:
        raise BadRequest("Content-Type must be application/json")
    
    data = request.get_json()
    form = ReminderForm(data=data)
    
    if form.validate():
        reminder = Reminder.create(
            title=form.title.data,
            content=form.content.data,
            due_date=form.due_date.data,
            user_id=current_user.id,
        )
        current_app.logger.info(f"Reminder created via API: {reminder.title}")
        
        return jsonify({
            "message": "Reminder created successfully",
            "reminder": {
                "id": reminder.id,
                "title": reminder.title,
                "content": reminder.content,
                "due_date": reminder.due_date.isoformat(),
                "created_at": reminder.created_at.isoformat(),
                "completed": reminder.completed,
                "is_overdue": reminder.is_overdue
            }
        }), 201
    else:
        return jsonify({"errors": form.errors}), 400


@blueprint.route("/<int:reminder_id>", methods=["GET"])
@login_required
def get_reminder(reminder_id):
    """Get a specific reminder via API."""
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first()
    
    if not reminder:
        raise NotFound("Reminder not found")
    
    return jsonify({
        "reminder": {
            "id": reminder.id,
            "title": reminder.title,
            "content": reminder.content,
            "due_date": reminder.due_date.isoformat(),
            "created_at": reminder.created_at.isoformat(),
            "completed": reminder.completed,
            "is_overdue": reminder.is_overdue
        }
    }), 200


@blueprint.route("/<int:reminder_id>", methods=["PUT"])
@login_required
def update_reminder(reminder_id):
    """Update a reminder via API."""
    if not request.is_json:
        raise BadRequest("Content-Type must be application/json")
    
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first()
    if not reminder:
        raise NotFound("Reminder not found")
    
    data = request.get_json()
    form = ReminderForm(data=data, obj=reminder)
    
    if form.validate():
        form.populate_obj(reminder)
        db.session.commit()
        current_app.logger.info(f"Reminder updated via API: {reminder.title}")
        
        return jsonify({
            "message": "Reminder updated successfully",
            "reminder": {
                "id": reminder.id,
                "title": reminder.title,
                "content": reminder.content,
                "due_date": reminder.due_date.isoformat(),
                "created_at": reminder.created_at.isoformat(),
                "completed": reminder.completed,
                "is_overdue": reminder.is_overdue
            }
        }), 200
    else:
        return jsonify({"errors": form.errors}), 400


@blueprint.route("/<int:reminder_id>/complete", methods=["POST"])
@login_required
def complete_reminder(reminder_id):
    """Mark a reminder as complete via API."""
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first()
    if not reminder:
        raise NotFound("Reminder not found")
    
    reminder.completed = True
    db.session.commit()
    current_app.logger.info(f"Reminder completed via API: {reminder.title}")
    
    return jsonify({
        "message": "Reminder marked as complete",
        "reminder": {
            "id": reminder.id,
            "title": reminder.title,
            "completed": reminder.completed
        }
    }), 200


@blueprint.route("/<int:reminder_id>", methods=["DELETE"])
@login_required
def delete_reminder(reminder_id):
    """Delete a reminder via API."""
    reminder = Reminder.query.filter_by(id=reminder_id, user_id=current_user.id).first()
    if not reminder:
        raise NotFound("Reminder not found")
    
    title = reminder.title
    db.session.delete(reminder)
    db.session.commit()
    current_app.logger.info(f"Reminder deleted via API: {title}")
    
    return jsonify({"message": f"Reminder '{title}' deleted successfully"}), 200
