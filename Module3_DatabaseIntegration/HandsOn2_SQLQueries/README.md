# Hands-On 2: Writing SQL Queries — DML, Joins & Aggregations

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Data Manipulation Language (DML), Relational JOINs & Aggregations  

---

## 📋 Overview

This hands-on exercise populates the `college_db` relational database with canonical sample datasets, executes data mutations (`UPDATE`, `DELETE`), builds multi-table INNER and LEFT JOINs, and generates analytical summary reports using aggregate functions (`COUNT`, `AVG`, `ROUND`, `SUM`, `MAX`) with `GROUP BY` and `HAVING` filters.

---

## 📁 Files Included

- `01_insert_data.sql`: Data seeding script (Departments, Students, Courses, Enrollments, Professors + 2 Custom Students).
- `02_dml.sql`: Data manipulation statements (`UPDATE`, `DELETE`, `COUNT(*)` verification).
- `03_select_queries.sql`: Single-table queries (`WHERE`, `ORDER BY`, `LIKE`, `BETWEEN`).
- `04_join_queries.sql`: Multi-table relational queries (2-table, 3-table, LEFT JOIN missing relationships).
- `05_aggregate_queries.sql`: Summary reports using `GROUP BY`, `HAVING`, `ROUND(AVG())`.
- `README.md`: Exercise documentation.

---

## 🚀 Execution Instructions

### PostgreSQL
```bash
psql -U postgres -d college_db -f 01_insert_data.sql
psql -U postgres -d college_db -f 02_dml.sql
psql -U postgres -d college_db -f 03_select_queries.sql
psql -U postgres -d college_db -f 04_join_queries.sql
psql -U postgres -d college_db -f 05_aggregate_queries.sql
```
