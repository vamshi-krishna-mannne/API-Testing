import os

from flask import Flask

from DummyData import insert_dummy_data
from database import db

from routes import init_routes

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
if not os.path.exists('database.db'):
    with app.app_context():
        db.create_all()
        insert_dummy_data()
init_routes(app)
