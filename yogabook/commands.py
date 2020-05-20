from . import app, db
from flask.cli import AppGroup
from .models import Instructor, ClassType, Venue, Feature

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

    db.session.add_all(
        [sarah, jamie, daisy, bikram, vinyasa, inyengar, aerial, green_lake, old_hall, gallery, cafe, changing_room, parking, gym, swimming, mats])
    db.session.commit()


@seed_cli.command('clear')
def clear():
    print('clear')
    try:
        instructors = Instructor.query.all()
        classtypes = ClassType.query.all()
        venues = Venue.query.all()
        features = Feature.query.all()
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
    except:
        print('error')
        db.session.rollback()


app.cli.add_command(seed_cli)