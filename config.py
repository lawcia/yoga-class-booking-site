import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
FLASK_ENV = os.getenv('FLASK_ENV')

if FLASK_ENV == 'development':
  PASSWORD = os.getenv('PASSWORD')
  USER = os.getenv('USER')
  URI = f'postgres://{USER}:{PASSWORD}@localhost:5432/yogabook'
  debug = True
else: 
  URI = os.getenv('URL')
  debug = False

class Config(object):
  DEBUG = debug
  TESTING = False
  SQLALCHEMY_DATABASE_URI = URI
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOAD_FOLDER = basedir + '/assets'
  ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
