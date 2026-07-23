# Python Backend Frameworks Master Architectural Index

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Repository**: `PythonBackendFrameworks/`  

---

## 🗺️ Hands-On Modules Overview

| Module | Framework | Key Concepts & Deliverables |
| :--- | :--- | :--- |
| **Hands-On 1** | Django | Web framework foundations, project/app scaffold, `hello_view`, Request-Response cycle, WSGI vs. ASGI, MVC vs. MVT, and custom middleware classes (`notes.py`). |
| **Hands-On 2** | Django | Models (`Department`, `Course`, `Student`, `Enrollment`), `unique_together` constraints, migrations, `CourseAdmin` customization, and ORM query optimization (`shell_examples.py`). |
| **Hands-On 3** | Django REST Framework | `ModelSerializer`, APIViews, `ModelViewSet`, `DefaultRouter`, and custom detail action `@action` returning enrolled students. |
| **Hands-On 4** | Flask | Application Factory (`create_app`), `Config` class, `courses_bp` Blueprint, JSON envelope helpers, and custom JSON error handlers. |
| **Hands-On 5** | Flask & SQLAlchemy | Flask-SQLAlchemy models with `to_dict()`, Flask-Migrate integration, ORM CRUD, JOIN queries, and database seeding script. |
| **Hands-On 6** | FastAPI | Pydantic v2 schemas (`CourseCreate`, `CourseResponse`), nested schemas, async engine, `get_db` dependency injection, and automatic Swagger docs. |
| **Hands-On 7** | FastAPI | Full REST CRUD, HTTP status conventions (`201`, `204`, `404`), `BackgroundTasks` email simulation, and OpenAPI metadata customization. |
| **Hands-On 8** | RESTful API Design | Plural noun naming, semantic HTTP methods (GET, POST with `Location` header, PUT, PATCH, DELETE), `/api/v1/` versioning, offset pagination envelope, and search filters. |
| **Hands-On 9** | Auth & Security | `bcrypt` work-factor password hashing, `python-jose` JWT token generation, OAuth2 bearer dependency, user registration/login, protected routes, and CORS middleware. |
| **Hands-On 10** | Microservices | Service decomposition (Course Service on 5001, Student Service on 5002), inter-service HTTP communication with 503 fallback, and API Gateway proxy (5000). |
