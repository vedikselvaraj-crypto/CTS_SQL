"""
================================================================================
ASGI ASYNCHRONOUS SERVER ENTRY POINT (asgi.py)
================================================================================
ROLE OF THIS FILE:
Exposes the ASGI callable 'application' used by asynchronous web servers 
(such as Daphne, Uvicorn, or Hypercorn) to handle async connections, WebSockets, 
and long-polling channels.
================================================================================
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')
application = get_asgi_application()
