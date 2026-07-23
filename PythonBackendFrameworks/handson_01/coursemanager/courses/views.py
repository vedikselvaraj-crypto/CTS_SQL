"""
================================================================================
COURSES APPLICATION VIEWS (views.py)
================================================================================
Contains function-based views (FBVs) handling HTTP requests.
================================================================================
"""

from django.http import HttpRequest, HttpResponse


def hello_view(request: HttpRequest) -> HttpResponse:
    """Simple function-based view returning plain text confirmation status."""
    return HttpResponse("Course Management API is running", content_type="text/plain")
