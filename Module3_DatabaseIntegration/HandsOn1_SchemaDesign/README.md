# Hands-On 1: Schema Design & Core SQL — DDL and Normalization

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Relational Database Design, DDL & Normalization Analysis  

---

## 📋 Overview

This hands-on exercise designs the foundational relational schema (`college_db`) for the Student Course Registration System. It implements DDL scripts for 5 core tables with strict primary keys, foreign keys, uniqueness, and check constraints across both PostgreSQL and MySQL database engines, followed by a formal database normalization analysis (1NF, 2NF, 3NF).

---

## 📁 Files Included

- `01_create_database.sql`: Database creation commands.
- `02_create_tables.sql`: DDL for `departments`, `students`, `courses`, `enrollments`, and `professors`.
- `03_alter_tables.sql`: Schema evolution DDL (`ADD`, `ALTER`, `CHECK`, `RENAME`, `DROP`).
- `normalization_analysis.md`: Formal theoretical breakdown of 1NF, 2NF, 3NF compliance.
- `README.md`: Exercise documentation.

---

## 🚀 Execution Instructions

### PostgreSQL
```bash
psql -U postgres -f 01_create_database.sql
psql -U postgres -d college_db -f 02_create_tables.sql
psql -U postgres -d college_db -f 03_alter_tables.sql
```

### MySQL
```bash
mysql -u root -p < 01_create_database.sql
mysql -u root -p college_db < 02_create_tables.sql
mysql -u root -p college_db < 03_alter_tables.sql
```
