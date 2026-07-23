# Module 3: Database Integration — PostgreSQL, MySQL & MongoDB Master Suite

![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.0-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.3-orange.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)
![Alembic](https://img.shields.io/badge/Alembic-1.13-purple.svg)

This repository contains the complete, production-grade implementation of all 108 hands-on tasks from the **Digital Nurture 5.0 - Python Full Stack Engineer Track (Module 3: Database Integration)**.

All exercises model an enterprise **Student Course Registration System** (`college_db`), progressing from relational DDL/DML, normalization analysis, subqueries, views, stored procedures, transactions, query optimization, and indexes, to MongoDB NoSQL document modeling, SQLAlchemy ORM, and Alembic schema migrations.

---

##  Entity-Relationship (ER) Diagram (ASCII Architecture)

```text
  +-------------------+              +-------------------+
  |    DEPARTMENTS    | 1          * |     PROFESSORS    |
  +-------------------+--------------+-------------------+
  | PK department_id  |<--+          | PK professor_id   |
  |    dept_name      |   |          |    prof_name      |
  |    head_of_dept   |   |          |    email          |
  |    budget         |   |          | FK department_id  |
  +-------------------+   |          |    salary         |
         | 1              |          +-------------------+
         |                |
         |                +------------------------------+
         | *                                             |
  +-------------------+              +-------------------+
  |      COURSES      | 1          * |      STUDENTS     |
  +-------------------+--------------+-------------------+
  | PK course_id      |              | PK student_id     |
  |    course_name    |              |    first_name     |
  |    course_code    |              |    last_name      |
  |    credits        |              |    email          |
  | FK department_id  |              |    date_of_birth  |
  +-------------------+              | FK department_id  |
         | 1                         |    enrollment_year|
         |                           +-------------------+
         | *                                | 1
  +-----------------------------------------+
  | *
  +-------------------+
  |    ENROLLMENTS    |  (Junction Table)
  +-------------------+
  | PK enrollment_id  |
  | FK student_id     |
  | FK course_id      |
  |    enrollment_date|
  |    grade          |
  +-------------------+
  UNIQUE(student_id, course_id)
```

---

##  Project Structure

```text
Module3_DatabaseIntegration/
│
├── README.md                           # Master repository documentation
├── requirements.txt                    # Consolidated Python dependencies
├── .gitignore                          # Git ignore configuration
├── docs/                               # Architectural index & documentation
│   └── index.md
│
├── HandsOn1_SchemaDesign/              # Relational DDL, Constraints & Normalization (1NF-3NF)
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_alter_tables.sql
│   ├── normalization_analysis.md
│   └── README.md
│
├── HandsOn2_SQLQueries/                # DML Data Population, Joins & Aggregations
│   ├── 01_insert_data.sql
│   ├── 02_dml.sql
│   ├── 03_select_queries.sql
│   ├── 04_join_queries.sql
│   ├── 05_aggregate_queries.sql
│   └── README.md
│
├── HandsOn3_AdvancedSQL/               # Subqueries, Views, Stored Procedures & Transactions
│   ├── 01_subqueries.sql
│   ├── 02_views.sql
│   ├── 03_procedures.sql
│   ├── 04_transactions.sql
│   └── README.md
│
├── HandsOn4_QueryOptimization/         # EXPLAIN Query Plans, Indexing & N+1 Problem Benchmarks
│   ├── optimization.sql
│   ├── n_plus_one.py
│   └── README.md
│
├── HandsOn5_MongoDB/                   # NoSQL BSON Modelling, CRUD & Aggregation Pipeline
│   ├── mongo_setup.js
│   ├── crud_operations.js
│   ├── aggregation_pipeline.js
│   ├── indexes.js
│   └── README.md
│
├── HandsOn6_SQLAlchemyORM/             # SQLAlchemy 2.0 ORM, Relationships & Eager Loading
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── queries.py
│   └── README.md
│
└── HandsOn7_AlembicMigration/          # Alembic Database Schema Migrations & Safe Rollbacks
    ├── alembic.ini
    ├── models.py
    ├── migration_commands.md
    ├── alembic/
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions/
    │       ├── 001_initial_schema.py
    │       ├── 002_add_is_active_to_students.py
    │       └── 003_add_course_schedules_table.py
    └── README.md
```

---

## Installation & Database Setup

### 1. Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

---

### 2. Database Server Configurations

#### PostgreSQL Setup
```bash
# Connect to PostgreSQL CLI
psql -U postgres

# Create Database
CREATE DATABASE college_db;
\c college_db
```

#### MySQL Setup
```sql
-- Connect to MySQL CLI
mysql -u root -p

-- Create Database
CREATE DATABASE college_db;
USE college_db;
```

#### MongoDB Setup
```bash
# Start MongoDB Daemon or Connect via mongosh
mongosh

# Switch to database
use college_nosql
```

---

##  Execution Guide by Module

### Running SQL Scripts (PostgreSQL / MySQL)
```bash
# PostgreSQL Execution
psql -U postgres -d college_db -f HandsOn1_SchemaDesign/02_create_tables.sql
psql -U postgres -d college_db -f HandsOn2_SQLQueries/01_insert_data.sql

# MySQL Execution
mysql -u root -p college_db < HandsOn1_SchemaDesign/02_create_tables.sql
mysql -u root -p college_db < HandsOn2_SQLQueries/01_insert_data.sql
```

### Running N+1 Performance Benchmark
```bash
cd HandsOn4_QueryOptimization
python n_plus_one.py
```

### Running MongoDB JavaScript Scripts
```bash
mongosh college_nosql HandsOn5_MongoDB/mongo_setup.js
mongosh college_nosql HandsOn5_MongoDB/crud_operations.js
mongosh college_nosql HandsOn5_MongoDB/aggregation_pipeline.js
```

### Running SQLAlchemy ORM Scripts
```bash
cd HandsOn6_SQLAlchemyORM
python crud.py
python queries.py
```

### Running Alembic Database Migrations
```bash
cd HandsOn7_AlembicMigration
alembic upgrade head
alembic history --verbose
alembic downgrade -1
alembic upgrade head
```

---

## Database Normalization Overview (1NF to 3NF)

1. **First Normal Form (1NF)**: Every column holds atomic, non-indivisible values. No repeating groups or arrays stored in CSV strings.
2. **Second Normal Form (2NF)**: Satisfies 1NF, and every non-key column is fully functionally dependent on the primary key (no partial dependencies on composite keys).
3. **Third Normal Form (3NF)**: Satisfies 2NF, and eliminates all transitive dependencies ($\text{Key} \to \text{Non-Key A} \to \text{Non-Key B}$).

---

##  Submission Instructions

```bash
git add .
git commit -m "Feat: Complete Module 3 Database Integration (Hands-On 1 to 7)"
git push origin main
```
