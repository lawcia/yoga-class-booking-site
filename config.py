import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)


PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER')


SQLALCHEMY_DATABASE_URI = f'postgres://{USER}:{PASSWORD}@localhost:5432/yogabook'
