"""
================================================================================
FLASK CONFIGURATION (config.py)
================================================================================
"""

import os


class Config:
    """Central Flask Configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask-handson04-secret-key-12345')
    DEBUG = True
    JSON_SORT_KEYS = False
