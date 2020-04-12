import json
import os

from flask import Flask
from .database import db
from .models import User
from .routes import init_routes

def create_dummy_users():
    with open('users.json') as file:
        data = json.load(file)
    for user_item in data:
        if User.query.filter_by(username=user_item['username']).first() is not None:
            return "dummy users already created"
        user = User(username=user_item['username'])
        user.email = user_item['email']
        user.hash_password(user_item['password'])
        db.session.add(user)
        db.session.commit()
    return "dummy users created successfully"

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
if not os.path.exists('database.db'):
    with app.app_context():
        db.create_all()
        create_dummy_users()
init_routes(app)


