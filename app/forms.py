# Python file for Form classes
# Contains moels to determine the data being captured by the forms
# and the logic whether they have been filled in correctly

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, RadioField, BooleanField, SelectField, SelectMultipleField, widgets, Form, FormField
from wtforms.validators import DataRequired, Email, InputRequired 
import pycountry


class TestForm(FlaskForm):

    # Test details
    name = StringField('Static name')


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class UserDetailsForm(FlaskForm):

    # Contact details
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Contact email', validators=[Email(message=('Not a valid email address.')), DataRequired()])
    pronoun = SelectField('Pronoun', choices=[('she', 'she/her'), ('he', 'he/him'), ('they', 'they/them'), ('per', 'per/per'), ('ae', 'ae/aer'), ('ey', 'ey/em'), ('ve', 've/ver'), ('xe', 'xe/xem'), ('zie', 'zie/hir')], validators=[InputRequired()])
    
    country_choices = [(country.alpha_2, country.name) for country in pycountry.countries]
    country = SelectField('Country of Location', choices=country_choices)

    # Consent options
    agree_data = BooleanField('By checking this box I agree to kotikoulu holding the data submitted for the purpose intended. I understand I can ask for my data to be removed at any time by emailing kotikoulu.', validators=[InputRequired()])
    agree_contact = BooleanField('By checking this box I agree to kotikoulu giving an appropriately matched caregiver the email address given above, along with my name and preferred pronouns.', validators=[InputRequired()])
    agree_safety = BooleanField('By checking this box I agree that I am aware of the safety issues inherent with using an online service and kotikoulu take no responsibility once the match is made.', validators=[InputRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


# Create python class for the offer (volunteer) form
class OfferForm(UserDetailsForm):

    # Teaching exp options
    teaching = RadioField('Do you have any teaching experience?', choices=[('1', 'Yes'), ('0', 'No')], validators=[DataRequired()])
    teaching_exp = StringField('What teaching experience do you have?')
    teaching_help = RadioField('Would you be interested in helping other volunteers?', choices=[('1', 'Yes'), ('0', 'No')], validators=[DataRequired()])

    # Volunteering options
    help_type = MultiCheckboxField('Commnication style', choices=[('video', 'Video calls'), ('resources', 'Making/providing resources')])
    help_freq = MultiCheckboxField('Frequency', choices=[('one', 'One-off'), ('many', 'Regular')])
    other_subjects = StringField('Pop your languages and other subjects here.')
    enrichment = StringField('If you have a particular project that you\'d love to talk about, or anything else to add, pop it here.', widget=widgets.TextArea())


# Create python class for the call (caregiver) form
class CallForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])


class SubjectsForm():

    confidence_choices = [('0', 'Not at all'), ('1', 'Up to 9'), ('2', 'Up to 13'), ('3', 'Up to 16'), ('4', 'Up to 18')]

    def __init__(self, record):    
        # add dynamic fields
        for key, value in record.items():
            setattr(OfferForm, key, RadioField(value, choices=self.confidence_choices))