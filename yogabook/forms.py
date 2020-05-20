from wtforms import SelectField, validators, SubmitField, SelectMultipleField, RadioField
from flask_wtf import FlaskForm

class CreateInstructorForm(FlaskForm):
  name = SelectField('Name', choices=[('Alex Heart', 'Alex Heart'), ('Sam Doe', 'Sam Doe'), ('Noah Smith', 'Noah Smith'), ('Toyah Tyler', 'Toyah Tyler')])
  city = SelectField('City', choices=[('london', 'London'), ('bristol', 'Bristol'), ('brighton', 'Brighton')])
  phone = SelectField('Phone', choices=[('07801000000','07801000000'), ('07802000000','07802000000'), ('07803000000','07803000000'), ('07804000000','07804000000'), ('07805000000','07805000000')])
  email = SelectField('Email', choices=[
    ('yogamaster@mail.com', 'yogamaster@mail.com'),
    ('fityoga@mail.com', 'fityoga@mail.com'),
    ('yoga@mail.com', 'yoga@mail.com'),
    ('ayogateacher@mail.com', 'ayogateacher@mail.com')
  ])
  instagram = SelectField('Instagram', choices=[
    ('https://insta.com/yoga', 'https://insta.com/yoga'),
     ('https://insta.com/angelyoga', 'https://insta.com/angelyoga'),
        ('https://insta.com/downwarddog', 'https://insta.com/downwarddog'),
           ('https://insta.com/spinningturtle', 'https://insta.com/spinningturtle'),
              ('https://insta.com/missmryoga', 'https://insta.com/missmryoga')
  ])
  class_types = SelectMultipleField('Class Types', [validators.DataRequired()], choices=[
    ('Bikram', 'Bikram'), ('Vinyasa', 'Vinyasa'), ('Iyengar', 'Iyengar'), ('Aerial', 'Aerial'), ('Yin', 'Yin')
  ])
  pictures = RadioField('Picture', choices=[('/images/woman_in_sun.jpg', 'Picture 1'), ('/images/woman_hand_pose.jpg', 'Picture 2'), ('/images/man_sweater.jpg', 'Picture 3'), ('/images/woman_sunglasses.jpg', 'Picture 4')], default='/images/woman_in_sun.jpg')
  submit = SubmitField(label='Create Instructor')
  