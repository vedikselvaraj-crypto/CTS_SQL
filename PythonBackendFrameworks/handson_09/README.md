# Hands-On 9: Authentication & Security — JWT, OAuth2 & OWASP

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Web API Security, Password Hashing, JWT Bearer Auth & CORS  

---

## 📋 Overview

This hands-on exercise implements enterprise-grade API security:
- **`bcrypt` Password Hashing**: Work-factor key stretching via `passlib`.
- **JWT Token Authentication**: Signed RS256/HS256 tokens via `python-jose` with 30-minute expiration.
- **OAuth2 Dependency Injection**: Protected endpoint access (`Depends(get_current_user)`).
- **Cross-Origin Resource Sharing (CORS)**: Configured for `http://localhost:3000`.
- **OWASP Top 10 Security**: In-code documentation and mitigations.

---

## 📁 Directory Structure

```text
handson_09/
├── README.md
├── requirements.txt
├── auth.py                             # JWT token creation & OAuth2 bearer dependency
├── database.py                         # Async database setup
├── main.py                             # FastAPI app & CORSMiddleware configuration
├── models.py                           # User & Course ORM models
├── schemas.py                          # User & Auth Pydantic schemas
├── security.py                         # Passlib bcrypt password hashing utilities
└── routers/
    ├── auth_router.py                  # Register & Login endpoints
    └── courses_router.py               # Protected Course endpoints
```

---

## 🚀 Testing Authentication Flow

### 1. Register User (`POST /api/v1/auth/register/`)
```json
{
  "email": "user@college.edu",
  "password": "SecurePassword123!"
}
```
**Expected Status**: `201 Created`

### 2. Login (`POST /api/v1/auth/login/`)
Submit Form-Data or JSON credentials.  
**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Access Protected Route (`POST /api/v1/courses/`)
- Without Header -> `401 Unauthorized`
- Header `Authorization: Bearer <TOKEN>` -> `201 Created`
