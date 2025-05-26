# -*- coding: utf-8 -*-
"""Reminder-related scheduled jobs."""
import datetime as dt
from flask import current_app

from app.models import Reminder, User
from app.extensions import db


def check_overdue_reminders():
    """Check for overdue reminders and log them."""
    with current_app.app_context():
        overdue_reminders = Reminder.query.filter(
            Reminder.due_date < dt.datetime.now(dt.timezone.utc),
            Reminder.completed == False
        ).all()
        
        if overdue_reminders:
            current_app.logger.info(f"Found {len(overdue_reminders)} overdue reminders")
            for reminder in overdue_reminders:
                current_app.logger.info(
                    f"Overdue reminder: '{reminder.title}' for user {reminder.user.username}"
                )
        else:
            current_app.logger.debug("No overdue reminders found")


def send_reminder_notifications():
    """Send notifications for upcoming reminders (placeholder for future email/SMS functionality)."""
    with current_app.app_context():
        # Find reminders due in the next hour
        one_hour_from_now = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)
        upcoming_reminders = Reminder.query.filter(
            Reminder.due_date <= one_hour_from_now,
            Reminder.due_date > dt.datetime.now(dt.timezone.utc),
            Reminder.completed == False
        ).all()
        
        if upcoming_reminders:
            current_app.logger.info(f"Found {len(upcoming_reminders)} upcoming reminders")
            for reminder in upcoming_reminders:
                current_app.logger.info(
                    f"Upcoming reminder: '{reminder.title}' for user {reminder.user.username}"
                )
                # TODO: Implement actual notification sending (email, SMS, etc.)
        else:
            current_app.logger.debug("No upcoming reminders found")
