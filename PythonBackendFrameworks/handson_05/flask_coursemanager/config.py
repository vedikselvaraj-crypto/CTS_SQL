"""
================================================================================
FLASK CONFIGURATION WITH DATABASE URI (config.py)
================================================================================
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuration class specifying SQLite database path."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask-handson05-secret-key-67890')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'coursemanager.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
