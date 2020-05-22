from . import app, db
from flask.cli import AppGroup
from .models import Instructor, ClassType, Venue, Feature, YogaClass
from datetime import datetime

seed_cli = AppGroup('seed')

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
    gallery = Venue(name="Gallery", city="Bristol", phone="07600000000", img_link="/images/gallery.jpg",
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

    yoga_class = YogaClass(class_start=datetime(2020, 5, 22, 17), class_end=datetime(2020, 5, 22, 19))
    yoga_class.instructor = sarah
    yoga_class.venue = gallery
    yoga_class1 = YogaClass(class_start=datetime(2020, 5, 27, 17), class_end=datetime(2020, 5, 27, 19))
    yoga_class1.instructor = sarah
    yoga_class1.venue = gallery
    yoga_class2 = YogaClass(class_start=datetime(2020, 5, 22, 17,30), class_end=datetime(2020, 5, 22, 19, 30))
    yoga_class2.instructor = jamie
    yoga_class2.venue = old_hall
    yoga_class3 = YogaClass(class_start=datetime(2020, 6, 1, 17, 30), class_end=datetime(2020, 6, 1, 19, 30))
    yoga_class3.instructor = jamie
    yoga_class3.venue = old_hall
    yoga_class4 = YogaClass(class_start=datetime(2020, 7, 5, 14), class_end=datetime(2020, 7, 5, 15))
    yoga_class4.instructor = daisy
    yoga_class4.venue = green_lake

    db.session.add_all(
        [sarah, jamie, daisy, bikram, vinyasa, inyengar, aerial, green_lake, old_hall, gallery, cafe, changing_room, parking, gym, swimming, mats, yoga_class, yoga_class1, yoga_class2, yoga_class3, yoga_class4])
    db.session.commit()


@seed_cli.command('clear')
def clear():
    print('clear')
    try:
        instructors = Instructor.query.all()
        classtypes = ClassType.query.all()
        venues = Venue.query.all()
        features = Feature.query.all()
        yogaclasses = YogaClass.query.all()
        for yogaclass in yogaclasses:
            db.session.delete(yogaclass)
        for instructor in instructors:
            db.session.delete(instructor)
        for classtype in classtypes:
            db.session.delete(classtype)
        for venue in venues:
            db.session.delete(venue)
        for feature in features:
            db.session.delete(feature)
        db.session.commit()
        print('done')
    except ValueError:
        print(ValueError)
        print('error')
        db.session.rollback()


app.cli.add_command(seed_cli)