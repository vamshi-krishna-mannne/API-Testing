
from flask import request, jsonify, url_for

from auth import auth
from database import db
from .models import User


def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    if username is None or password is None or email is None:
        return "username or password or email fields are required"  # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        return "username is already taken"  # existing user
    user = User(username=username)
    user.email = email
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    return (jsonify("user created", {'username': user.username}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})

@auth.login_required
def get_all_users():
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in User.query.all()])

@auth.login_required
def get_user(id):
    user = User.query.get(id)
    if not user:
        return "user is not registered yet"
    return jsonify({'username': user.username})



