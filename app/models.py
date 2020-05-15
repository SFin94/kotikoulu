""" Defines database models """

from app import db
from flask import current_app # as app - Not sure on due to next line


class Volunteer(db.Model):

    __tablename__ = "volunteers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    pronoun = db.Column(db.String(10), nullable=False, unique=False)
    country = db.Column(db.String(32), nullable=True, unique=False)

    teaching = db.Column(db.Boolean, nullable=False, unique=False)
    teaching_exp = db.Column(db.Text, nullable=True, unique=False)
    teaching_help = db.Column(db.Boolean, nullable=True, unique=False)

    help_calls = db.Column(db.Boolean, nullable=False, unique=False)
    help_resources = db.Column(db.Boolean, nullable=False, unique=False)
    sc_maths = db.Column(db.Float, nullable=True, unique=False)
    
    other_sub = db.Column(db.Text, nullable=True, unique=False)
    enrichment = db.Column(db.Text, nullable=True, unique=False)

    def __repr__(self):
        return "{}".format(self.name)

# class Caregiver():




        

