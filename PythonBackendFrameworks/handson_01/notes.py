"""
================================================================================
HANDS-ON 1: WEB FRAMEWORK FOUNDATIONS & ARCHITECTURAL DEEP DIVE
================================================================================

1. THE HTTP REQUEST-RESPONSE CYCLE IN DJANGO:
--------------------------------------------------------------------------------
When a web browser or client sends an HTTP request (e.g. GET /api/courses/) to a 
Django application, it traverses through the following sequential architecture:

  [Client Browser]
        │ (1) HTTP Request
        ▼
  [Web Server / WSGI Gateway (e.g. Gunicorn/uWSGI)]
        │ (2) Converts HTTP bytes to Python WSGI environment dict
        ▼
  [Django Middleware Pipeline (Request Processors)]
        │ (3) Executes SecurityMiddleware, SessionMiddleware, CommonMiddleware, etc.
        ▼
  [URL Dispatcher (coursemanager/urls.py)]
        │ (4) Matches URL path regex/string to target View function
        ▼
  [View Layer (courses/views.py)]
        │ (5) Processes business logic, parses request parameters
        ▼
  [Model / Database Layer (courses/models.py)]
        │ (6) Executes SQL queries via Django ORM to retrieve/mutate data
        ▼
  [Response Construction (HttpResponse / JsonResponse)]
        │ (7) Formats data payload into HTTP response object
        ▼
  [Django Middleware Pipeline (Response Processors)]
        │ (8) Adds CORS headers, sets cookies, compresses payload
        ▼
  [Client Browser] <--- Returns HTTP Status 200 OK + JSON Payload

================================================================================
2. MIDDLEWARE ARCHITECTURE & CUSTOM MIDDLEWARE IMPLEMENTATIONS:
--------------------------------------------------------------------------------
Middleware is a framework of hooks into Django's request/response processing. 
It is a light, low-level plugin system for globally altering Django's input or output.

Built-in Middleware Examples:
a) django.middleware.security.SecurityMiddleware:
   - Enhances HTTP security by setting X-Content-Type-Options: nosniff, 
     enforcing SSL/HTTPS redirects, and configuring Strict-Transport-Security.
b) django.middleware.csrf.CsrfViewMiddleware:
   - Protects against Cross-Site Request Forgery attacks by injecting and 
     verifying hidden cryptographic CSRF tokens on state-changing requests (POST/PUT).
"""

import time
import logging
from typing import Callable
from django.http import HttpRequest, HttpResponse

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Custom Middleware Class 1: Request Execution Timing & Logging Middleware
# ------------------------------------------------------------------------------
class RequestLoggingMiddleware:
    """Middleware that logs incoming HTTP request method, path, and total execution latency."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        start_time = time.time()
        
        # Process request through downstream middleware and view
        response = self.get_response(request)
        
        duration = (time.time() - start_time) * 1000  # Convert to milliseconds
        print(f"[LOG] {request.method} {request.path} - Status: {response.status_code} ({duration:.2f}ms)")
        return response


# ------------------------------------------------------------------------------
# Custom Middleware Class 2: Custom API Header Middleware
# ------------------------------------------------------------------------------
class CustomHeaderMiddleware:
    """Middleware that injects custom architectural metadata headers into every HTTP response."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        response["X-Framework-Author"] = "Senior Backend Architect"
        response["X-Course-API-Version"] = "1.0.0"
        return response


"""
================================================================================
3. WSGI VS. ASGI COMPARISON:
--------------------------------------------------------------------------------
WSGI (Web Server Gateway Interface - PEP 3333):
- Synchronous Python web server standard.
- Operates on a synchronous request-per-thread model. Handles requests one-by-one 
  per worker process.
- Default in standard Django deployments.
- Limitation: Poor performance for long-lived connections (WebSockets, Server-Sent Events).

ASGI (Asynchronous Server Gateway Interface):
- Modern asynchronous standard extending WSGI.
- Built on Python's asyncio event loop. Supports async/await natively.
- Handles thousands of concurrent long-lived connections (WebSockets, HTTP/2, streaming).
- When to switch to ASGI: When your app requires real-time messaging, WebSockets, 
  background streaming tasks, or async database queries.

================================================================================
4. MVC VS. MVT PATTERN ARCHITECTURE:
--------------------------------------------------------------------------------
Standard MVC (Model-View-Controller):
- Model: Handles data schema and database interactions.
- View: Renders the user interface (HTML/UI components).
- Controller: Contains business logic, receives user input, and updates Model & View.

Django's MVT (Model-View-Template):
- Model (M): Maps directly to MVC Model. Defines database tables via Django ORM.
- View (V): Corresponds to MVC Controller! Contains business logic, handles HTTP 
  requests, queries models, and returns HTTP responses.
- Template (T): Corresponds to MVC View! Handles presentation layer (HTML/Jinja-like rendering).
================================================================================
"""
