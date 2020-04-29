# Python file for Form classes
# Contains moels to determine the data being captured by the forms
# and the logic whether they have been filled in correctly

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email 


# Create python class for the offer (volunteer) form
class OfferForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Contact email', validators=[Email(message=('Not a valid email address.')), DataRequired()])
    country = StringField('Country of Location')
    # helptype = 
    # recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

# Create python class for the call (caregiver) form
class CallForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])