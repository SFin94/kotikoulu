# Python file for Form classes
# Contains moels to determine the data being captured by the forms
# and the logic whether they have been filled in correctly

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, RadioField, BooleanField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, InputRequired 


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class TestForm(FlaskForm):

    # Test details
    test = MultiCheckboxField('Commnication style', choices=[('Video calls', 'video'), ('Making/providing resources', 'resources')])
    # , widget=widgets.CheckboxInput())
    # test = SelectMultipleField('Commnication style', choices=[('Video calls', 'video'), ('Making/providing resources', 'resources')], widget=widgets.CheckboxInput())


# Create python class for the offer (volunteer) form
class OfferForm(FlaskForm):

    # Volunteer details
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Contact email', validators=[Email(message=('Not a valid email address.')), DataRequired()])
    pronoun = SelectField('Pronoun', choices=[('she', 'she/her'), ('he', 'he/him'), ('they', 'they/them'), ('per', 'per/per'), ('ae', 'ae/aer'), ('ey', 'ey/em'), ('ve', 've/ver'), ('xe', 'xe/xem'), ('zie', 'zie/hir')], validators=[InputRequired()])
    country = StringField('Country of Location')
    teaching_exp = BooleanField('Do you have any teaching experience?')

    # Teaching exp options


    # Volunteering options
    help_type = MultiCheckboxField('Commnication style', choices=[('video', 'Video calls'), ('resources', 'Making/providing resources')])
    help_freq = MultiCheckboxField('Frequency', choices=[('one', 'One-off'), ('many', 'Regular')])
    

    # Consent options
    agree_data = BooleanField('By checking this box I agree to kotikoulu holding the data submitted for the purpose intended. I understand I can ask for my data to be removed at any time by emailing kotikoulu.', validators=[InputRequired()])
    agree_contact = BooleanField('By checking this box I agree to kotikoulu giving an appropriately matched caregiver the email address given above, along with my name and preferred pronouns.', validators=[InputRequired()])
    agree_safety = BooleanField('By checking this box I agree that I am aware of the safety issues inherent with using an online service and kotikoulu take no responsibility once the match is made.', validators=[InputRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

# Create python class for the call (caregiver) form
class CallForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])