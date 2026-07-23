"""
================================================================================
ROOT URL ROUTER CONFIGURATION (urls.py)
================================================================================
ROLE OF THIS FILE:
Acts as the central URL routing dispatch table for the entire Django project.
Maps incoming HTTP request URL paths (e.g. /admin/, /api/) to views or delegates 
to app-level urlconfs using include().
================================================================================
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Delegate /api/ requests to the courses application URL configuration
    path('api/', include('courses.urls')),
]
