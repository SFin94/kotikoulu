""" Routes for what a user should be served when visiting the url within the app"""

from flask import Flask, render_template, request, redirect, url_for
from flask import current_app as app

from .forms import OfferForm

# Start route
@app.route('/')
def home():
    title = 'kotikoulu'
    description = 'Helping with homeschooling'
    return render_template('home.html', title=title, description=description)


# Route: offer/volunteer form
@app.route('/offerform', methods=('GET', 'POST'))
def offer():
    form = OfferForm()
    if form.validate_on_submit():
        return redirect(url_for('kiitos'))
    return render_template('form_offer.html', form=form, title='Volunteer form')
