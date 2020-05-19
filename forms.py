from wtforms import Form, StringField, validators

class CreateInstructorForm(Form):
  name = StringField('Name', [validators.Length(min=2, max=300), validators.DataRequired('You must enter a name')])
  