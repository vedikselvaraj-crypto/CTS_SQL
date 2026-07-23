# Hands-On 6: FastAPI — Path Parameters, Pydantic & Async Endpoints

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Modern High-Performance FastAPI Framework  

---

## 📋 Overview

This hands-on exercise scaffolds a modern FastAPI application utilizing Pydantic v2 schemas (`CourseCreate`, `CourseUpdate`, `CourseResponse`, nested `DepartmentResponse`), async/await non-blocking endpoints, path/query parameter automatic validation, Async SQLAlchemy 2.0 database access, and auto-generated Swagger UI documentation.

---

## 📁 Directory Structure

```text
handson_06/
├── README.md
├── requirements.txt
├── database.py                         # Async SQLAlchemy Engine & Session Maker
├── dependencies.py                     # get_db() Dependency Injection
├── main.py                             # FastAPI App & Async Route Handlers
├── models.py                           # Async SQLAlchemy Declarative Models
└── schemas.py                          # Pydantic Request / Response Models
```

---

## 🚀 Execution & Testing Instructions

### 1. Launch FastAPI Server via Uvicorn
```bash
cd handson_06
uvicorn main:app --reload --port 8000
```

### 2. Access Auto-Generated Interactive API Documentation
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc UI**: `http://127.0.0.1:8000/redoc`

### 3. Test Async Pagination & Filtering
- Pagination: `GET http://127.0.0.1:8000/api/courses/?skip=0&limit=2`
- Department Filter: `GET http://127.0.0.1:8000/api/courses/?department_id=1`
