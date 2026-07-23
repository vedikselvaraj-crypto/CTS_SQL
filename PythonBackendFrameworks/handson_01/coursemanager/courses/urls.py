"""
================================================================================
COURSES APPLICATION URL ROUTING (urls.py)
================================================================================
"""

from django.urls import path
from courses.views import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello_view'),
]
