from . import db

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
    name = db.Column(db.String(300), nullable=False, unique=True)
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
    name = db.Column(db.String(300), nullable=False, unique=True)
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