# Hands-On 1: Web Framework Foundations & Django Project Setup

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Django Project Scaffolding & Web Fundamentals  

---

## 📋 Overview

This hands-on exercise establishes the core theoretical and practical foundations of Python web backend development. It covers the HTTP request-response cycle, Django's architecture, WSGI vs. ASGI server protocols, middleware pipelines, and MVC vs. MVT pattern mappings.

---

## 📁 Directory Structure

```text
handson_01/
├── README.md
├── requirements.txt
├── notes.py                            # Comprehensive architectural notes & custom middleware
└── coursemanager/                      # Scaffolding Django Project
    ├── manage.py
    ├── coursemanager/
    │   ├── __init__.py
    │   ├── settings.py                # Project configuration & INSTALLED_APPS
    │   ├── urls.py                    # Root URL router delegating to app
    │   ├── wsgi.py                    # WSGI entry point
    │   └── asgi.py                    # ASGI entry point
    └── courses/                        # Modular Django App
        ├── __init__.py
        ├── apps.py
        ├── admin.py
        ├── models.py
        ├── views.py                   # Contains hello_view function
        └── urls.py                    # App-level URL dispatcher
```

---

## 🚀 Execution & Setup Instructions

### 1. Run Development Server
```bash
cd handson_01/coursemanager
python manage.py runserver 8000
```

### 2. Verify Endpoint
Open browser or Postman and access:
`http://127.0.0.1:8000/api/hello/`

**Expected Response**:
`"Course Management API is running"`
