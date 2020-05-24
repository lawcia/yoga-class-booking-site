from wtforms import SelectField, validators, SubmitField, SelectMultipleField, RadioField, ValidationError, IntegerField, DateTimeField
from flask_wtf import FlaskForm
from .models import Instructor, Venue, YogaClass
from . import db


class CreateInstructorForm(FlaskForm):
    name = SelectField('Name', choices=[('Alex Heart', 'Alex Heart'),
                                        ('Sam Doe', 'Sam Doe'),
                                        ('Noah Smith', 'Noah Smith'),
                                        ('Toyah Tyler', 'Toyah Tyler')])
    city = SelectField('City', choices=[('london', 'London'),
                                        ('bristol', 'Bristol'),
                                        ('brighton', 'Brighton')])
    phone = SelectField('Phone', choices=[('07801000000', '07801000000'),
                                          ('07802000000', '07802000000'),
                                          ('07803000000', '07803000000'),
                                          ('07804000000', '07804000000'),
                                          ('07805000000', '07805000000')])
    email = SelectField('Email', choices=[('yogamaster@mail.com', 'yogamaster@mail.com'),
                                          ('fityoga@mail.com', 'fityoga@mail.com'),
                                          ('yoga@mail.com', 'yoga@mail.com'),
                                          ('ayogateacher@mail.com', 'ayogateacher@mail.com')])
    instagram = SelectField('Instagram', choices=[('https://insta.com/yoga',
                                                   'https://insta.com/yoga'),
                                                  ('https://insta.com/angelyoga',
                                                   'https://insta.com/angelyoga'),
                                                  ('https://insta.com/downwarddog',
                                                   'https://insta.com/downwarddog'),
                                                  ('https://insta.com/spinningturtle',
                                                   'https://insta.com/spinningturtle'),
                                                  ('https://insta.com/missmryoga',
                                                   'https://insta.com/missmryoga')
                                                  ])
    class_types = SelectMultipleField('Class Types', [validators.DataRequired()],
                                      choices=[('Bikram', 'Bikram'),
                                               ('Vinyasa', 'Vinyasa'),
                                               ('Iyengar', 'Iyengar'),
                                               ('Aerial', 'Aerial'),
                                               ('Yin', 'Yin')])
    pictures = RadioField('Picture', choices=[('/images/woman_in_sun.jpg', 'Picture 1'),
                                              ('/images/woman_hand_pose.jpg',
                                               'Picture 2'),
                                              ('/images/man_sweater.jpg',
                                               'Picture 3'),
                                              ('/images/woman_sunglasses.jpg', 'Picture 4')],
                          default='/images/woman_in_sun.jpg')
    submit = SubmitField(label='Create Instructor')

    def validate_name(self, field):
        if Instructor.query.filter_by(name=field.data).first():
            raise ValidationError('This name has been taken')

    def validate_phone(self, field):
        if Instructor.query.filter_by(phone=field.data).first():
            raise ValidationError('This phone number has been taken')

    def validate_email(self, field):
        if Instructor.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been taken')


class CreateVenueForm(FlaskForm):
    name = SelectField('Name', [validators.DataRequired()], choices=[('Fitwind', 'Fitwind'),
                                                                     ('Yoga Primed',
                                                                      'Yoga Primed'),
                                                                     ('Studio Heritage',
                                                                      'Studio Heritage'),
                                                                     ('Studiolaza',
                                                                      'Studiolaza'),
                                                                     ('Fit Shape', 'Fit Shape')])
    city = SelectField('City', [validators.DataRequired()], choices=[('London', 'London'),
                                                                     ('Brighton',
                                                                      'Brighton'),
                                                                     ('Bristol', 'Bristol')])
    phone = SelectField('Phone', choices=[('03801000000', '03801000000'),
                                          ('03802000000', '03802000000'),
                                          ('03803000000', '03803000000'),
                                          ('03804000000', '03804000000'),
                                          ('03805000000', '03805000000')])
    email = SelectField('Email', choices=[('kickstart@mail.com', 'kickstart@mail.com'),
                                          ('studio@mail.com', 'studio@mail.com'),
                                          ('venue@mail.com', 'venue@mail.com'),
                                          ('yogadome@mail.com', 'yogadome@mail.com')])
    instagram = SelectField('Instagram', choices=[('https://insta.com/studio',
                                                   'https://insta.com/studio'),
                                                  ('https://insta.com/venue',
                                                   'https://insta.com/venue'),
                                                  ('https://insta.com/azure',
                                                   'https://insta.com/azure'),
                                                  ('https://insta.com/fitshape',
                                                   'https://insta.com/fitshape'),
                                                  ('https://insta.com/yogaadora',
                                                   'https://insta.com/yogaadora')
                                                  ])
    features = SelectMultipleField('Features', [validators.DataRequired()],
                                      choices=[('Cafe', 'Cafe'),
                                               ('Changing room', 'Changing room'),
                                               ('Parking', 'Parking'),
                                               ('Gym', 'Gym'),
                                               ('Swimming pool', 'Swimming pool'),
                                               ('Mats', 'Mats')])
    capacity = IntegerField('Capacity', [validators.DataRequired('Please enter a number')])
    pictures = RadioField('Picture', choices=[('/images/old_lost_hall.jpg', 'Picture 1'),
                                              ('/images/gym_dark.jpg',
                                               'Picture 2'),
                                              ('/images/future_hall.jpg',
                                               'Picture 3'),
                                              ('/images/old_gym.jpg', 'Picture 4')],
                          default='/images/old_lost_hall.jpg')
    submit = SubmitField(label='Create Venue')

    def validate_name(self, field):
        if Venue.query.filter_by(name=field.data).first():
            raise ValidationError('This venue name has been taken')

    def validate_phone(self, field):
        if Venue.query.filter_by(phone=field.data).first():
            raise ValidationError('This phone number has been taken')

    def validate_email(self, field):
        if Venue.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been taken')

    def validate_capacity(self, field):
        if field.data < 10 or field.data > 500:
            raise ValidationError('Please enter a capacity between 10 and 500')


class CreateClassForm(FlaskForm):
    instructor_id = IntegerField('Instructor ID', [validators.DataRequired('Please enter an instructor ID')])
    venue_id = IntegerField('Venue ID', [validators.DataRequired('Please enter a venue ID')])
    start_time = DateTimeField('Class date & time', [validators.DataRequired('Please enter a start time')])
    duration = IntegerField('Class duration', [validators.DataRequired('Please enter a class duration')])
    frequency = SelectField('Frequency', [validators.DataRequired()], choices=[('once', 'once'), 
    ('weekly', 'weekly'),
    ('monthly', 'monthly')])
    submit = SubmitField(label='Promote Class')

    def validate_instructor_id(self, field):
        if not Instructor.query.get(field.data):
            raise ValidationError('Please enter a valid instructor ID')
    
    def validate_venue_id(self, field):
        if not Venue.query.get(field.data):
            raise ValidationError('Please enter a valid venue ID')

    def validate_duration(self, field):
        if field.data > 1440:
            raise ValidationError('Duration can\'t be more than 1 day')
        elif field.data < 0:
            raise ValidationError('Duration can\'t be less than 0')

