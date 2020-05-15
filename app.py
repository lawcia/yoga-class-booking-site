from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import AppGroup
from werkzeug.utils import secure_filename

app = Flask(__name__)
seed_cli = AppGroup('seed')
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


instructor_class_type = db.Table('instructor_class_type',
                                 db.Column('instructor_id', db.Integer,
                                           db.ForeignKey('instructor.id'), primary_key=True),
                                 db.Column('class_type_id', db.Integer,
                                           db.ForeignKey('class_type.id'), primary_key=True)
                                 )

venue_feature = db.Table('venue_feature',
                         db.Column('venue_id', db.Integer, db.ForeignKey(
                             'venue.id'), primary_key=True),
                         db.Column('feature_id', db.Integer, db.ForeignKey(
                             'feature.id'), primary_key=True)
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


class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    img_link = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    insta_link = db.Column(db.String(500), nullable=True)
    capacity = db.Column(db.Integer, nullable=False)
    features = db.relationship(
        'Feature', secondary=venue_feature, lazy='subquery', backref=db.backref('venues', lazy=True)
    )


class Feature(db.Model):
    __tablename__ = 'feature'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)


@seed_cli.command('seed')
def seed():
    sarah = Instructor(name="Sarah Den", city="London", phone="00000000000",
                       img_link="/images/sarahden.jpg", email="sarahden@mail.com", insta_link="https://insta.com/sarahden")
    jamie = Instructor(name="Jamie Kart", city="London", phone="00000000001",
                       img_link="/images/jamiekart.jpg", email="jamiekart@mail.com", insta_link="https://insta.com/jamiedoesyoga")
    daisy = Instructor(name="Daisy Meadow", city="Bristol", phone="00000000005",
                       img_link="/images/daisymeadow.jpg", email="daisymeadow@mail.com", insta_link="https://insta.com/missmeadow")
    bikram = ClassType(title="Bikram")
    vinyasa = ClassType(title="Vinyasa")
    inyengar = ClassType(title="Iyengar")
    aerial = ClassType(title="Aerial")
    yin = ClassType(title="Yin")
    green_lake = Venue(name="Green Lake", city="London", phone="07800000000", img_link="/images/park.jpg",
                       email="greenlake@mail.com", insta_link="https://insta.com/greenlake", capacity=300)
    old_hall = Venue(name="Old Hall", city="London", phone="07500000000", img_link="/images/glass_window_hall.jpg",
                     email="oldhall@mail.com", insta_link="https://insta.com/oldhall", capacity=60)
    gallery = Venue(name="Gallery", city="Bristol", phone="07600000000", img_link="/images/gallery",
                    email="bristolgallery@mail.com", insta_link="https://insta.com/bristolgallery", capacity=20)
    cafe = Feature(description="Cafe")
    changing_room = Feature(description="Changing room")
    parking = Feature(description="Parking")
    gym = Feature(description="Gym")
    swimming = Feature(description="Swimming pool")
    mats = Feature(description="Mats")

    sarah.class_types.extend([bikram, vinyasa, yin])
    jamie.class_types.extend([vinyasa, inyengar, yin])
    daisy.class_types.extend([vinyasa, aerial])
    old_hall.features.extend([changing_room, mats, parking])
    green_lake.features.extend([swimming, parking, cafe])
    gallery.features.extend([mats, gym, changing_room])

    db.session.add_all(
        [sarah, jamie, daisy, bikram, vinyasa, inyengar, aerial, green_lake, old_hall, gallery, cafe, changing_room, parking, gym, swimming, mats])
    db.session.commit()


@seed_cli.command('clear')
def clear():
    print('clear')
    try:
        instructors = Instructor.query.all()
        classtypes = ClassType.query.all()
        for instructor in instructors:
            db.session.delete(instructor)
        for classtype in classtypes:
            db.session.delete(classtype)
        db.session.commit()
        print('done')
    except:
        print('error')
        db.session.rollback()


app.cli.add_command(seed_cli)


@app.route('/')
def index():
    return render_template('pages/home.html')


@app.route('/instructors')
def list_instructors():
    return render_template('pages/instructors.html', instructors=Instructor.query.all())


@app.route('/instructors/<id>')
def instructor(id):
    return render_template('pages/instructor.html', instructor=Instructor.query.get(id))


@app.route('/images/<filename>')
def uploaded_img(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run()
