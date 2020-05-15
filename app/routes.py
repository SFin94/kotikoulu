""" Routes for what a user should be served when visiting the url within the app"""

from flask import render_template, request, redirect, url_for, make_response
from flask import current_app as app

from .forms import OfferForm, TestForm, SubjectsForm
from .models import db, Volunteer

subject_list = {'math': 'Maths','chem': 'Chemistry','biol': 'Biology', 'phys': 'Physics', 'elit': 'English Literature', 'elan': 'English Language', 'geog': 'Geography', 'hist': 'History','dram': 'Drama','art': 'Art','musi': 'Music','lang': 'Languages (please state below)','othr': 'Other (please state below)'}

# Start route
@app.route('/')
def home():
    title = 'kotikoulu'
    return render_template('home.html', title=title)

@app.route('/kiitos')
def kiitos():
    return render_template('kiitos.html')


# Route: offer/volunteer form
@app.route('/offerform', methods=('GET', 'POST'))
def offer():
    SubjectsForm(subject_list)
    form = OfferForm()
    if form.validate_on_submit():
        form_data = request(form)
        return redirect(url_for('kiitos'))
    return render_template('form_offer.html', form=form, subjects=subject_list, title='Volunteer form')


@app.route('/test', methods=('GET', 'POST'))
def test():
    subject_list = {'maths': 'Mathematics', 'physics': 'Physics'}
    # TestSubjects(subject_list)
    form = TestForm()
    return render_template('test.html', form=form, subjects=subject_list)


@app.route('/testdb', methods=['GET'])
def testdb():

    name = request.args.get('nome')
    if name:
        new_volunteer = Volunteer(name=name, email='test@test.com', pronoun='he/him', teaching=False, help_calls=True, help_resources=False, sc_maths=3)
        db.session.add(new_volunteer)
        db.session.commit()
    return make_response(f"{new_volunteer} successfully created!")