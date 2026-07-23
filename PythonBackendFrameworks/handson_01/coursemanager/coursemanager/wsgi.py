"""
================================================================================
WSGI SERVER GATEWAY ENTRY POINT (wsgi.py)
================================================================================
ROLE OF THIS FILE:
Exposes the WSGI callable 'application' used by synchronous web deployment servers 
(such as Gunicorn, uWSGI, or Apache mod_wsgi) to forward HTTP requests to Django.
================================================================================
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')
application = get_wsgi_application()
