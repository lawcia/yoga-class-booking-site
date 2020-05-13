from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import AppGroup

app = Flask(__name__)
seed_cli = AppGroup('seed')
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Models

instructor_class_type = db.Table('instructor_class_type',
                                 db.Column('instructor_id', db.Integer,
                                           db.ForeignKey('instructor.id'), primary_key=True),
                                 db.Column('class_type_id', db.Integer,
                                           db.ForeignKey('class_type.id'), primary_key=True)
                                 )


class Instructor(db.Model):
    __tablename__ = 'instructor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    img_link = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    insta_link = db.Column(db.String(500), nullable=True)
    class_types = db.relationship(
        'ClassType', secondary=instructor_class_type, lazy='subquery', backref=db.backref('instructors', lazy=True))


class ClassType(db.Model):
    __tablename__ = 'class_type'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, unique=True)


@seed_cli.command('seed')
def seed():
    sarah = Instructor(name="Sarah Den", city="London", phone="00000000000",
                       img_link="https://test.com", email="sarahden@mail.com", insta_link="https://insta.com/sarahden")
    jamie = Instructor(name="Jamie Kart", city="London", phone="00000000001",
                       img_link="https://test.com", email="jamiekart@mail.com", insta_link="https://insta.com/jamiedoesyoga")
    daisy = Instructor(name="Daisy Meadow", city="Bristol", phone="00000000005",
                       img_link="https://test.com", email="daisymeadow@mail.com", insta_link="https://insta.com/missmeadow")
    bikram = ClassType(title="Bikram")
    vinyasa = ClassType(title="Vinyasa")
    inyengar = ClassType(title="Iyengar")
    aerial = ClassType(title="Aerial")
    yin = ClassType(title="Yin")
    sarah.class_types.extend([bikram, vinyasa, yin])
    jamie.class_types.extend([vinyasa, inyengar, yin])
    daisy.class_types.extend([vinyasa, aerial])
    db.session.add_all(
        [sarah, jamie, daisy, bikram, vinyasa, inyengar, aerial])
    db.session.commit()


@seed_cli.command('clear')
def clear():
    try:
        db.session.query(Instructor).delete()
        db.session.query(ClassType).delete()
        db.session.commit()
    except:
        db.session.rollback()


app.cli.add_command(seed_cli)


@app.route('/')
def index():
    return render_template('pages/home.html')

@app.route('/instructors')
def list_instructors(): 
    return render_template('pages/instructors.html', instructors = Instructor.query.all())

@app.route('/instructors/<id>')
def instructor(id):
    return render_template('pages/instructor.html', instructor = Instructor.query.get(id))

if __name__ == '__main__':
    app.run()
