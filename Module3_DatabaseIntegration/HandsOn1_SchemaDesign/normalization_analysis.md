# Database Normalization Analysis (1NF, 2NF, 3NF)

**System**: Student Course Registration System (`college_db`)  
**Author**: Principal Database Architect  

---

## 📐 1. First Normal Form (1NF) Analysis

### 1NF Requirements
1. Each column must hold **atomic (indivisible) values**.
2. There must be no repeating groups or multi-valued arrays stored in a single field.
3. Each record must be uniquely identifiable via a Primary Key.

### Verification in `college_db`
- All table attributes (`first_name`, `email`, `credits`, `grade`) store single scalar values.
- **Hypothetical Violation Avoided**: If we had stored multiple student phone numbers as a comma-separated CSV string (e.g. `phone_number = "555-0192, 555-0193"`) inside the `students` table, 1NF would be violated. To maintain 1NF, multi-valued attributes are placed into a separate child table (`student_phones`) or stored as atomic individual rows.

---

## 📐 2. Second Normal Form (2NF) Analysis

### 2NF Requirements
1. The table must satisfy 1NF.
2. Every non-key attribute must be **fully functionally dependent** on the **entire Primary Key** (no partial dependencies on a subset of a composite primary key).

### Verification in `college_db`
- In `students`, `courses`, `departments`, and `professors`, the primary key is a single surrogate integer (`student_id`, `course_id`, etc.). Partial dependencies are impossible when the primary key consists of a single attribute.
- **Junction Table Analysis (`enrollments`)**:
  - Composite Candidate Key: `(student_id, course_id)`.
  - Non-Key Attributes: `enrollment_date`, `grade`.
  - Both `enrollment_date` and `grade` depend on **both** the student AND the course (i.e. Grade 'A' belongs specifically to Student $S_1$ in Course $C_1$). Neither attribute depends on `student_id` alone nor `course_id` alone.
  - Hence, **no partial dependency exists**, and 2NF is satisfied.

---

## 📐 3. Third Normal Form (3NF) Analysis

### 3NF Requirements
1. The table must satisfy 2NF.
2. There must be **no transitive dependencies** (where a non-key attribute depends on another non-key attribute, i.e. $X \to Y$ and $Y \to Z$).

### Verification in `college_db`
- **Hypothetical Violation Avoided**: If we had stored `dept_name` and `head_of_dept` directly inside the `students` table:
  $$\text{student\_id} \to \text{department\_id} \to \text{dept\_name}$$
  This would create a transitive dependency where `dept_name` depends on `department_id`, which depends on `student_id`. Updating a department name would require updating every student row, causing update anomalies.
- **Resolution**: `departments` was extracted into an independent parent table. `students` holds only `department_id` as a Foreign Key.

---

## 📝 4. In-Depth 3NF Analysis of `enrollments` Table

```sql
-- 3NF ANALYSIS FOR ENROLLMENTS TABLE:
-- Primary Key: enrollment_id (Surrogate Key)
-- Composite Candidate Key: (student_id, course_id)
-- Non-Key Attributes: enrollment_date, grade
--
-- Functional Dependencies:
-- 1. enrollment_id -> student_id, course_id, enrollment_date, grade
-- 2. (student_id, course_id) -> enrollment_id, enrollment_date, grade
--
-- Conclusion: All non-key attributes (enrollment_date, grade) depend ONLY on the primary key.
-- No non-key attribute determines any other non-key attribute.
-- Therefore, enrollments is strictly in Third Normal Form (3NF).
```
