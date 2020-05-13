from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Models

class Instructor(db.Model):
  __tablename__ = 'instructor'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300), nullable=False)
  city = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  img_link = db.Column(db.String(500), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  insta_link = db.Column(db.String(500), nullable=True)
  class_types = db.relationship("ClassType", backref="instructor", lazy=True)


class ClassType(db.Model):
  __tablename__ = 'class_type'
  id = db.Column(db.Integer, primary_key=True)
  class_type = db.Column(db.Integer, nullable=False)
  instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))



@app.route('/')
def index():
  return render_template('pages/home.html')


if __name__ == '__main__':
  app.run()