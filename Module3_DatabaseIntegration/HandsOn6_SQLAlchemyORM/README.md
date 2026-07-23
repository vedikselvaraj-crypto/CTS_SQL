# Hands-On 6: ORM Integration — SQLAlchemy & Django ORM

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: SQLAlchemy 2.0 ORM, Relationships, Sessions & Eager Loading Optimizations  

---

## 📋 Overview

This hands-on exercise implements a Python backend module using **SQLAlchemy 2.0 ORM**:
- **ORM Models**: `Department`, `Student`, `Course`, `Enrollment`, `Professor` mapped via `DeclarativeBase`.
- **Relationship Navigation**: Bidirectional `relationship` attributes with `back_populates`.
- **Session API & CRUD**: Session lifecycle management (`Session`, `commit()`, `rollback()`, `delete()`).
- **N+1 Performance Mitigation**: Benchmarking lazy-loaded queries vs. eager loading using `joinedload()`, demonstrating a query reduction from 13 queries down to 1 SQL statement.

---

## 📁 Files Included

- `config.py`: Database connection settings & URI configuration.
- `database.py`: SQLAlchemy `create_engine` (with `echo=True` SQL logging) and `sessionmaker`.
- `models.py`: 5 ORM model classes with relationship properties.
- `crud.py`: Full ORM CRUD operations script.
- `queries.py`: N+1 query benchmark script comparing lazy loading vs `joinedload` eager loading.
- `README.md`: Exercise documentation.

---

## 🚀 Execution Instructions

### 1. Run Full ORM CRUD Script
```bash
cd HandsOn6_SQLAlchemyORM
python crud.py
```

### 2. Run Eager Loading N+1 Benchmark Script
```bash
python queries.py
```
