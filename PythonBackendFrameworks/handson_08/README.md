# Hands-On 8: RESTful API Design Best Practices

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Enterprise REST API Standards, Versioning, Pagination & Error Specifications  

---

## 📋 Overview

This hands-on exercise audits and refactors existing endpoints to follow industry-standard **RESTful best practices**:
- **Plural Noun Resource Naming**: `/api/v1/courses/`, `/api/v1/students/`
- **Semantic HTTP Methods**: GET, POST (with `Location` response header), PUT (full replace), PATCH (partial update), DELETE
- **API Versioning**: `/api/v1/` route prefix & in-code architectural comparison
- **DRF-Style Offset Pagination**: `page` & `page_size` parameters with count/next/previous envelope
- **Case-Insensitive Search Filtering**: `search=` parameter matching title and code
- **Standardized JSON Error Envelopes**: `{"error": {"code": "NOT_FOUND", "message": "...", "field": null}}`

---

## 📁 Directory Structure

```text
handson_08/
├── README.md
├── requirements.txt
├── database.py                         # Async SQLAlchemy setup
├── main.py                             # FastAPI app & standardized exception handlers
├── models.py                           # ORM models
├── schemas.py                          # Standardized error & paginated envelope schemas
└── routers/
    └── v1_courses.py                   # V1 Courses router with PATCH, Search & Pagination
```

---

## 🚀 Execution & Verification Instructions

### 1. Start FastAPI Server
```bash
cd handson_08
uvicorn main:app --reload --port 8000
```

### 2. Verify Paginated Response Envelope
`GET http://127.0.0.1:8000/api/v1/courses/?page=1&page_size=2`
```json
{
  "count": 5,
  "next": "http://127.0.0.1:8000/api/v1/courses/?page=2&page_size=2",
  "previous": null,
  "results": [...]
}
```

### 3. Verify Standardized Error Response Envelope
`GET http://127.0.0.1:8000/api/v1/courses/999/`
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Course with id 999 does not exist",
    "field": null
  }
}
```
