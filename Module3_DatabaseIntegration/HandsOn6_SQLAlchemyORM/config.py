"""
================================================================================
SQLALCHEMY CONFIGURATION (config.py)
================================================================================
"""

import os

# Default SQLite database path for zero external dependency execution
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(BASE_DIR, 'college_db_orm.db')
