# Hands-On 7: FastAPI — Dependency Injection, Full CRUD & OpenAPI Customization

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Advanced FastAPI REST Architecture & Async Background Workers  

---

## 📋 Overview

This hands-on exercise implements full RESTful CRUD for Courses, Students, and Enrollments following strict HTTP status code standards (`201 Created`, `204 No Content`, `404 Not Found`). It showcases **FastAPI BackgroundTasks** for non-blocking confirmation email dispatch and customizes OpenAPI metadata, tags, summaries, and field descriptions.

---

## 📁 Directory Structure

```text
handson_07/
├── README.md
├── requirements.txt
├── database.py                         # Async SQLAlchemy engine & session maker
├── dependencies.py                     # Reusable dependency injection helpers
├── main.py                             # Main app, OpenAPI customization & routers
├── models.py                           # Department, Course, Student, Enrollment ORM
├── schemas.py                          # Pydantic validation & response schemas
└── routers/                            # Modular APIRouter modules
    ├── courses.py
    ├── enrollments.py                  # BackgroundTasks implementation
    └── students.py
```

---

## 🚀 Testing & Execution Instructions

### 1. Launch FastAPI Server
```bash
cd handson_07
uvicorn main:app --reload --port 8000
```

### 2. Verify OpenAPI Documentation
Open `http://127.0.0.1:8000/docs` to inspect grouped tags (`Courses`, `Students`, `Enrollments`), customized titles, contact info, and response descriptions.

### 3. Verify Background Tasks
Send `POST http://127.0.0.1:8000/api/enrollments/` with JSON body:
```json
{
  "student_id": 1,
  "course_id": 1
}
```
- Endpoint returns `201 Created` instantly.
- Check terminal console output: `[BACKGROUND TASK] Sending confirmation email to alice@college.edu...`
