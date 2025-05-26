# -*- coding: utf-8 -*-
"""API authentication endpoints."""
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import BadRequest, Unauthorized

from app.forms import LoginForm, RegisterForm
from app.models import User
from app.extensions import db, limiter

blueprint = Blueprint("api_auth", __name__, url_prefix="/api/auth")


@blueprint.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    """API login endpoint."""
    if not request.is_json:
        raise BadRequest("Content-Type must be application/json")

    data = request.get_json()
    form = LoginForm(data=data)

    if form.validate():
        login_user(form.user)
        current_app.logger.info(f"User {form.user.username} logged in via API")
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": form.user.id,
                "username": form.user.username,
                "email": form.user.email
            }
        }), 200
    else:
        return jsonify({"errors": form.errors}), 400


@blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    """API logout endpoint."""
    username = current_user.username
    logout_user()
    current_app.logger.info(f"User {username} logged out via API")
    return jsonify({"message": "Logout successful"}), 200


@blueprint.route("/register", methods=["POST"])
@limiter.limit("3 per hour")
def register():
    """API user registration endpoint."""
    if not request.is_json:
        raise BadRequest("Content-Type must be application/json")

    data = request.get_json()
    form = RegisterForm(data=data)

    if form.validate():
        user = User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        current_app.logger.info(f"New user registered via API: {user.username}")
        return jsonify({
            "message": "Registration successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 201
    else:
        return jsonify({"errors": form.errors}), 400


@blueprint.route("/me", methods=["GET"])
@login_required
def me():
    """Get current user information."""
    return jsonify({
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "first_name": current_user.first_name,
            "last_name": current_user.last_name,
            "active": current_user.active,
            "is_admin": current_user.is_admin
        }
    }), 200
