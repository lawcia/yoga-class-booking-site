from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask.cli import with_appcontext

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# register_commands(app)

# Models

instructor_class_type = db.Table( 'instructor_class_type',
  db.Column('instructor_id', db.Integer, db.ForeignKey('instructor.id')),
  db.Column('class_type_id', db.Integer, db.ForeignKey('class_type.id'))
)

class Instructor(db.Model):
  __tablename__ = 'instructor'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300), nullable=False)
  city = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  img_link = db.Column(db.String(500), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  insta_link = db.Column(db.String(500), nullable=True)
  class_types = db.relationship('ClassType', secondary=instructor_class_type, backref='instructors')

class ClassType(db.Model):
  __tablename__ = 'class_type'
  id = db.Column(db.Integer, primary_key=True)
  class_type = db.Column(db.Integer, nullable=False)



# @with_appcontext
# def seed():
#   instructor1 = Instructor(name="Sarah Den", city="London", phone="00000000000", img_link="https://test.com", email="sarahden@mail.com", insta_link="https://insta.com")
#   instructor2 = Instructor(name="Jamie Kart", city="London", phone="00000000001", img_link="https://test.com", email="jamiekart@mail.com", insta_link="https://insta.com")
#   instructor3 = Instructor(name="Daisy Meadow", city="Bristol", phone="00000000005", img_link="https://test.com", email="daisymeadow@mail.com", insta_link="https://insta.com")


# def register_commands(app):
#   """Register CLI commands."""
#   app.cli.add_command(seed)

@app.route('/')
def index():
  return render_template('pages/home.html')


if __name__ == '__main__':
  app.run()