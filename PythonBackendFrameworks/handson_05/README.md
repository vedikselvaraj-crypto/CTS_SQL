# Hands-On 5: Flask with Flask-SQLAlchemy ORM & Database Integration

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Flask-SQLAlchemy Database ORM & Migrations  

---

## 📋 Overview

This hands-on exercise connects the Flask Course Management API to a real relational SQLite database using **Flask-SQLAlchemy** and **Flask-Migrate**. It defines ORM models (`Department`, `Course`, `Student`, `Enrollment`), `to_dict()` serialization, relationship navigation (`back_populates`), and SQL JOIN queries.

---

## 📁 Directory Structure

```text
handson_05/
├── README.md
├── requirements.txt
└── flask_coursemanager/
    ├── app.py                         # App factory & Flask-Migrate init
    ├── config.py                      # SQLite database URI configuration
    ├── database.py                    # SQLAlchemy instance (db = SQLAlchemy())
    ├── models.py                      # Department, Course, Student, Enrollment
    ├── seed_db.py                     # Database seeding script
    └── courses/
        ├── __init__.py
        └── routes.py                  # ORM database routes & JOIN queries
```

---

## 🚀 Setup & Execution Instructions

### 1. Seed Database & Create Tables
```bash
cd handson_05/flask_coursemanager
python seed_db.py
```

### 2. Run Flask API Server
```bash
python app.py
```

### 3. Test Endpoints
- Get All Courses: `GET http://127.0.0.1:5000/api/courses/`
- Get Enrolled Students via JOIN Query: `GET http://127.0.0.1:5000/api/courses/1/students/`
