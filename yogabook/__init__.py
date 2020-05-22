import os
from flask import Flask
from flask.cli import AppGroup
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
migrate = Migrate(app, db, directory=os.path.join(basedir, 'migrations'))


from . import views, commands

