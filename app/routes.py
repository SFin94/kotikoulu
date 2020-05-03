""" Routes for what a user should be served when visiting the url within the app"""

from flask import render_template, request, redirect, url_for
from flask import current_app as app

from .forms import OfferForm, TestForm, SubjectsForm

subject_list = {'math': 'Maths','chem': 'Chemistry','biol': 'Biology', 'phys': 'Physics', 'elit': 'English Literature', 'elan': 'English Language', 'geog': 'Geography', 'hist': 'History','dram': 'Drama','art': 'Art','musi': 'Music','lang': 'Languages (please state below)','othr': 'Other (please state below)'}

# Start route
@app.route('/')
def home():
    title = 'kotikoulu'
    return render_template('home.html', title=title)

# Route: offer/volunteer form
@app.route('/offerform', methods=('GET', 'POST'))
def offer():
    SubjectsForm(subject_list)
    form = OfferForm()
    if form.validate_on_submit():
        return redirect(url_for('kiitos'))
    return render_template('form_offer.html', form=form, subjects=subject_list, title='Volunteer form')

@app.route('/test', methods=('GET', 'POST'))
def test():
    subject_list = {'maths': 'Mathematics', 'physics': 'Physics'}
    # TestSubjects(subject_list)
    form = TestForm()
    return render_template('test.html', form=form, subjects=subject_list)