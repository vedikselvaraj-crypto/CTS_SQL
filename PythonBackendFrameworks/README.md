# Python Backend Frameworks: Django, Flask & FastAPI Master Suite

![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0.0-green.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-teal.svg)
![Architecture](https://img.shields.io/badge/Architecture-Clean%20%2F%20Microservices-purple.svg)

This repository contains the complete implementation of all 104 hands-on exercises from the **Digital Nurture 5.0 - Python Full Stack Engineer Track (Python Backend Frameworks: Django, Flask & FastAPI)**.

All exercises build a unified business domain — a **Course Management API** — across Django, Flask, and FastAPI to compare framework paradigms, database ORMs, RESTful API design patterns, JWT authentication, and microservices decomposition.

---

## Repository Structure

```text
PythonBackendFrameworks/
│
├── README.md                           # Master project documentation
├── requirements.txt                    # Consolidated Python dependencies
├── .gitignore                          # Git ignore rule configuration
├── docs/                               # Master documentation index
│   └── index.md
│
├── handson_01/                         # Django Setup, MVT, WSGI/ASGI & Middleware
│   └── coursemanager/
│
├── handson_02/                         # Django Models, ORM Queries & Admin Interface
│   └── coursemanager/
│
├── handson_03/                         # Django REST Framework (DRF) Views, Routers & Serializers
│   └── coursemanager/
│
├── handson_04/                         # Flask App Factory, Blueprints & Error Handling
│   └── flask_coursemanager/
│
├── handson_05/                         # Flask with Flask-SQLAlchemy & Migrations
│   └── flask_coursemanager/
│
├── handson_06/                         # FastAPI Pydantic Schemas & Async SQLAlchemy
│   └── main.py
│
├── handson_07/                         # FastAPI Full CRUD, Background Tasks & OpenAPI Docs
│   └── main.py
│
├── handson_08/                         # RESTful API Design Best Practices (Versioning, Pagination)
│   └── main.py
│
├── handson_09/                         # JWT Authentication, Password Hashing & CORS
│   └── main.py
│
└── handson_10/                         # Microservices Architecture & API Gateway
    ├── course_service/                 # Independent Flask App (Port 5001)
    ├── student_service/                # Independent Flask App (Port 5002)
    └── gateway/                        # API Gateway Proxy (Port 5000)
```

---

##  Installation & Virtual Environment Setup

### 1. Create and Activate Virtual Environment

On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

##  How to Run Each Framework Project

### 1. Running Django Projects (Hands-On 1, 2, 3)

Navigate into the target Django project directory containing `manage.py`:

```bash
# Hands-On 1
cd handson_01/coursemanager
python manage.py runserver 8000

# Hands-On 2 (Migrations & ORM Shell)
cd handson_02/coursemanager
python manage.py makemigrations
python manage.py migrate
python manage.py shell < shell_examples.py
python manage.py runserver 8000

# Hands-On 3 (DRF API)
cd handson_03/coursemanager
python manage.py migrate
python manage.py runserver 8000
```
- Access API: `http://127.0.0.1:8000/api/courses/`
- Django Admin: `http://127.0.0.1:8000/admin/`

---

### 2. Running Flask Projects (Hands-On 4, 5)

```bash
# Hands-On 4
cd handson_04/flask_coursemanager
python app.py

# Hands-On 5 (Flask-SQLAlchemy & Migrations)
cd handson_05/flask_coursemanager
python seed_db.py
python app.py
```
- Access Flask API: `http://127.0.0.1:5000/api/courses/`

---

### 3. Running FastAPI Projects (Hands-On 6, 7, 8, 9)

```bash
# Hands-On 6
cd handson_06
uvicorn main:app --reload --port 8000

# Hands-On 9 (JWT Auth)
cd handson_09
uvicorn main:app --reload --port 8000
```
- Interactive Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc UI: `http://127.0.0.1:8000/redoc`

---

### 4. Running Microservices Architecture (Hands-On 10)

Launch each microservice in separate terminal windows:

```bash
# Terminal 1: Course Service (Port 5001)
cd handson_10/course_service
python app.py

# Terminal 2: Student Service (Port 5002)
cd handson_10/student_service
python app.py

# Terminal 3: API Gateway (Port 5000)
cd handson_10/gateway
python app.py
```

Test through Gateway Proxy:
- `GET http://localhost:5000/api/courses/` -> Proxies to Course Service (5001)
- `POST http://localhost:5000/api/students/1/enroll` -> Proxies to Student Service (5002) which calls Course Service.

---

##  Framework Architectural Comparison

| Metric / Feature | Django & DRF | Flask | FastAPI |
| :--- | :--- | :--- | :--- |
| **Philosophy** | Batteries-included, opinionated framework. | Lightweight, unopinionated micro-framework. | Modern, high-performance ASGI framework. |
| **ORM** | Django ORM (built-in). | Flask-SQLAlchemy / SQLAlchemy. | Async SQLAlchemy 2.0. |
| **Data Validation** | DRF Serializers. | Manual / Marshmallow. | Pydantic v2 (Rust-backed, instant validation). |
| **API Docs** | drf-spectacular / Manual. | Manual / Flasgger. | Automatic Swagger UI & ReDoc. |
| **Async Support** | Partial (ASGI supported). | WSGI (Flask 3.0 supports async views). | Native Async/Await via Starlette & Uvicorn. |

---

##  GitHub Submission Instructions

1. **Commit All Code**:
   ```bash
   git add .
   git commit -m "Feat: Complete Python Backend Frameworks Hands-On 1-10 implementation"
   ```
2. **Push to Remote Branch**:
   ```bash
   git push origin main
   ```
