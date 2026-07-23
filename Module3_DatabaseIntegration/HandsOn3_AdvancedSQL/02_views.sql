-- =============================================================================
-- HANDS-ON 3 - TASK 2: CREATING AND USING DATABASE VIEWS (02_views.sql)
-- Complex analytical views, GPA conversion CASE statements, & WITH CHECK OPTION
-- =============================================================================

-- Clean existing views
DROP VIEW IF EXISTS vw_course_stats CASCADE;
DROP VIEW IF EXISTS vw_student_enrollment_summary CASCADE;
DROP VIEW IF EXISTS vw_active_cs_students CASCADE;

-- -----------------------------------------------------------------------------
-- Step 39: Create view vw_student_enrollment_summary
-- Summarizes student details, department, course count, and GPA (A=4, B=3, C=2, D=1, F=0)
-- -----------------------------------------------------------------------------
CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    s.student_id, 
    CONCAT(s.first_name, ' ', s.last_name) AS student_full_name, 
    d.dept_name AS department, 
    COUNT(e.course_id) AS courses_enrolled_count, 
    ROUND(
        AVG(
            CASE e.grade
                WHEN 'A' THEN 4.0
                WHEN 'B' THEN 3.0
                WHEN 'C' THEN 2.0
                WHEN 'D' THEN 1.0
                WHEN 'F' THEN 0.0
                ELSE NULL
            END
        ), 2
    ) AS gpa 
FROM 
    students s 
INNER JOIN 
    departments d ON s.department_id = d.department_id 
LEFT JOIN 
    enrollments e ON s.student_id = e.student_id 
GROUP BY 
    s.student_id, s.first_name, s.last_name, d.dept_name;


-- -----------------------------------------------------------------------------
-- Step 40: Create view vw_course_stats
-- Summarizes course_name, course_code, total_enrollments, and avg_gpa
-- -----------------------------------------------------------------------------
CREATE VIEW vw_course_stats AS
SELECT 
    c.course_id, 
    c.course_name, 
    c.course_code, 
    COUNT(e.enrollment_id) AS total_enrollments, 
    ROUND(
        AVG(
            CASE e.grade
                WHEN 'A' THEN 4.0
                WHEN 'B' THEN 3.0
                WHEN 'C' THEN 2.0
                WHEN 'D' THEN 1.0
                WHEN 'F' THEN 0.0
                ELSE NULL
            END
        ), 2
    ) AS avg_gpa 
FROM 
    courses c 
LEFT JOIN 
    enrollments e ON c.course_id = e.course_id 
GROUP BY 
    c.course_id, c.course_name, c.course_code;


-- -----------------------------------------------------------------------------
-- Step 41: Query vw_student_enrollment_summary to find students with GPA > 3.0
-- -----------------------------------------------------------------------------
SELECT 
    student_id, 
    student_full_name, 
    department, 
    courses_enrolled_count, 
    gpa 
FROM 
    vw_student_enrollment_summary 
WHERE 
    gpa > 3.00 
ORDER BY 
    gpa DESC;


-- -----------------------------------------------------------------------------
-- Step 42: Updatable View Analysis Comment Block
-- -----------------------------------------------------------------------------
/*
================================================================================
UPDATABLE VIEW ANALYSIS & RESEARCH DOCUMENTATION:
--------------------------------------------------------------------------------
Attempting to execute an UPDATE on vw_student_enrollment_summary:
UPDATE vw_student_enrollment_summary SET student_full_name = 'Test Name' WHERE student_id = 1;

RESULT / ERROR:
SQL Error: Cannot update view 'vw_student_enrollment_summary' because it contains 
aggregate functions (COUNT, AVG), GROUP BY clauses, and multi-table JOINs.

WHY MULTI-TABLE AGGREGATE VIEWS ARE NOT UPDATABLE:
1. Ambiquity of Source Row: The Relational Engine cannot map an update on an 
   aggregated value (like GPA or courses_enrolled_count) back to a single 
   underlying physical tuple in the base database tables.
2. Rule of Updatable Views (SQL Standard): A view is updatable ONLY IF it references 
   a single base table, contains no aggregate functions, no DISTINCT, no GROUP BY, 
   no HAVING, and no set operations (UNION).
================================================================================
*/


-- -----------------------------------------------------------------------------
-- Step 43: Create a single-table subset view WITH CHECK OPTION
-- -----------------------------------------------------------------------------
CREATE VIEW vw_active_cs_students AS
SELECT 
    student_id, 
    first_name, 
    last_name, 
    email, 
    department_id, 
    enrollment_year 
FROM 
    students 
WHERE 
    department_id = 1 
WITH CHECK OPTION;

-- Test WITH CHECK OPTION: Inserting a student with department_id=1 succeeds.
-- Inserting department_id=2 fails with a CHECK OPTION violation error.
