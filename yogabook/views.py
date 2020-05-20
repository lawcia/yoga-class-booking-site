from flask import render_template, request, redirect, send_from_directory, flash
from . import app, db
from .models import Instructor, Venue, Feature, ClassType
from .forms import CreateInstructorForm

@app.route('/')
def index():
    return render_template('pages/home.html')


@app.route('/instructors')
def list_instructors():
    return render_template('pages/instructors.html', instructors=Instructor.query.all())

@app.route('/venues')
def list_venues():
    return render_template('pages/venues.html', venues=Venue.query.all())

@app.route('/instructors/create', methods=['GET', 'POST'])
def create_instructors():
    form = CreateInstructorForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            name = form.name.data
            city = form.city.data
            email = form.email.data
            phone = form.phone.data
            insta = form.instagram.data
            classes = form.class_types.data
            pic = form.pictures.data
            new_instructor = Instructor(name=name, city=city, phone=phone,
                       img_link=pic, email=email, insta_link=insta)
            for class_type in classes:
                new_class = ClassType.query.filter_by(title=class_type).first_or_404()
                new_instructor.class_types.append(new_class)
            db.session.add(new_instructor)
            db.session.commit()
        except Exception as error:
            flash('something went wrong!', 'message')
        else:
            flash('Instructor was successfully added!')
            return redirect('/')
        
    return render_template('forms/instructor.html', form=form)

@app.route('/instructors/<id>')
def instructor(id):
    return render_template('pages/instructor.html', instructor=Instructor.query.get(id))

@app.route('/venues/<id>')
def venue(id):
    return render_template('pages/venue.html', venue=Venue.query.get(id))

@app.route('/images/<filename>')
def uploaded_img(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500