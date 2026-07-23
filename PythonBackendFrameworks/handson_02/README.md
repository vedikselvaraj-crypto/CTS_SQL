# Hands-On 2: Django Models, ORM Queries & Admin Interface

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Django Object-Relational Mapping (ORM) & Admin Customization  

---

## 📋 Overview

This hands-on exercise implements full Django ORM models representing the Course Management domain (`Department`, `Course`, `Student`, `Enrollment`), enforces database constraints (`unique_together`), generates migration schemas, explores Django ORM query optimizations (`select_related`, `annotate`, `Count`, `F()` expressions), and customizes the Django Admin Interface.

---

## 📁 Directory Structure

```text
handson_02/
├── README.md
├── requirements.txt
└── coursemanager/
    ├── manage.py
    ├── shell_examples.py               # Executable ORM query script
    ├── coursemanager/
    │   ├── settings.py
    │   └── urls.py
    └── courses/
        ├── admin.py                    # Customized ModelAdmin views
        ├── models.py                   # Department, Course, Student, Enrollment
        └── migrations/
            └── 0001_initial.py         # DB Migration Schema
```

---

## 🚀 Execution & Testing Instructions

### 1. Apply Migrations
```bash
cd handson_02/coursemanager
python manage.py makemigrations
python manage.py migrate
```

### 2. Run ORM Shell Demonstration Script
```bash
python manage.py shell < shell_examples.py
```

### 3. Create Superuser & Access Django Admin
```bash
python manage.py createsuperuser --username admin --email admin@college.edu
python manage.py runserver 8000
```
Access Admin UI: `http://127.0.0.1:8000/admin/`
