# Hands-On 3: Advanced SQL — Subqueries, Views & Transactions

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Advanced SQL Concepts, Database Views, Stored Procedures & Transactions  

---

## 📋 Overview

This hands-on exercise implements advanced SQL querying techniques:
- **Subqueries**: Correlated subqueries, non-correlated subqueries, and derived tables in `FROM` clause.
- **Views**: Reusable database views (`vw_student_enrollment_summary`, `vw_course_stats`), GPA calculation using `CASE`, updatable view constraints, and `WITH CHECK OPTION`.
- **Stored Procedures & Functions**: MySQL `sp_enroll_student` & PostgreSQL `fn_enroll_student` with duplicate validation and transactional department transfers.
- **ACID Transactions**: `BEGIN`, `SAVEPOINT`, `ROLLBACK TO SAVEPOINT`, and `COMMIT` data integrity checkpoints.

---

## 📁 Files Included

- `01_subqueries.sql`: Advanced subquery techniques.
- `02_views.sql`: Database view definitions & updatable view constraints.
- `03_procedures.sql`: Stored procedures (MySQL) & PL/pgSQL functions (PostgreSQL).
- `04_transactions.sql`: ACID transaction & savepoint workflows.
- `README.md`: Exercise documentation.

---

## 🚀 Execution Instructions

### PostgreSQL
```bash
psql -U postgres -d college_db -f 01_subqueries.sql
psql -U postgres -d college_db -f 02_views.sql
psql -U postgres -d college_db -f 03_procedures.sql
psql -U postgres -d college_db -f 04_transactions.sql
```

### MySQL
```bash
mysql -u root -p college_db < 01_subqueries.sql
mysql -u root -p college_db < 02_views.sql
mysql -u root -p college_db < 03_procedures.sql
mysql -u root -p college_db < 04_transactions.sql
```
