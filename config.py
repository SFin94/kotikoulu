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

    # RECAPTCHA settings
    RECAPTCHA_PUBLIC_KEY = '6LdikPIUAAAAADhsjtdChwyQVAz59xPZEukPgUdt'
    RECAPTCHA_PRIVATE_KEY = '6LdikPIUAAAAAIEbHGVqLC7DvIzKGkiuk8G-WY2G'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True