"""Initialise app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    '''Function to construct core application'''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialise plugins
    db.init_app(app)

    # Manually push a context
    with app.app_context():
        # Import parts of our application
        from . import routes

        return app


# Old lines
# app.config['DEBUG'] = True
# app.conf['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/kkouludb'
# db = SQLAlchemy(app)