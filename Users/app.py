import os

from flask import Flask
from .database import db
from .routes import init_routes

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
if not os.path.exists('db.sqlite'):
    with app.app_context():
        db.create_all()
init_routes(app)
