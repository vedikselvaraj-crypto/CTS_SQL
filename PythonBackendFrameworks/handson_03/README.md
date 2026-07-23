# Hands-On 3: Django REST Framework (DRF) Views, Routers & Serializers

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Django REST Framework Architecture  

---

## 📋 Overview

This hands-on exercise converts the Django Course Management application into a full RESTful web API using Django REST Framework (DRF). It implements `ModelSerializer` classes, `APIView` class-based views, `ModelViewSet` viewsets, automatic `DefaultRouter` URL generation, and custom detail action endpoints.

---

## 📁 Directory Structure

```text
handson_03/
├── README.md
├── requirements.txt
└── coursemanager/
    ├── manage.py
    ├── coursemanager/
    │   ├── settings.py                # 'rest_framework' registered
    │   └── urls.py
    └── courses/
        ├── models.py
        ├── serializers.py             # Department, Course, Student, Enrollment serializers
        ├── views.py                   # APIViews & ModelViewSets with @action
        └── urls.py                    # DefaultRouter + APIView paths
```

---

## 🚀 API Endpoints Overview

| Endpoint | Method | Action / Description |
| :--- | :--- | :--- |
| `/api/courses/` | GET | List all courses (APIView & ViewSet) |
| `/api/courses/` | POST | Create a new course |
| `/api/courses/{id}/` | GET | Retrieve course detail |
| `/api/courses/{id}/` | PUT / PATCH | Update course |
| `/api/courses/{id}/` | DELETE | Remove course |
| `/api/courses/{id}/students/` | GET | **Custom Action**: List students enrolled in course |
| `/api/students/` | GET / POST | Student CRUD |
| `/api/enrollments/` | GET / POST | Enrollment CRUD |

---

## 🧪 Testing Instructions

```bash
cd handson_03/coursemanager
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```
- Interactive Browsable API: `http://127.0.0.1:8000/api/`
- Custom Enrolled Students Action: `http://127.0.0.1:8000/api/courses/1/students/`
