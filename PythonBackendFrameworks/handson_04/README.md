# Hands-On 4: Flask App Structure, Routing & Blueprints

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Flask Micro-Framework & Modular Architecture  

---

## 📋 Overview

This hands-on exercise implements a modular Flask backend application using the **Application Factory pattern** (`create_app()`), Flask **Blueprints** (`courses_bp`), environment configuration classes, JSON response envelopes, and custom JSON error handlers.

---

## 📁 Directory Structure

```text
handson_04/
├── README.md
├── requirements.txt
└── flask_coursemanager/
    ├── app.py                         # Application Factory & entry point
    ├── config.py                      # Config settings class
    └── courses/
        ├── __init__.py
        └── routes.py                  # Flask Blueprint & CRUD routes
```

---

## 🚀 Execution & Testing Instructions

```bash
cd handson_04/flask_coursemanager
python app.py
```
- API Base URL: `http://127.0.0.1:5000/api/courses/`
