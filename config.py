"""App configuration."""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database Config
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/kkouludb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False