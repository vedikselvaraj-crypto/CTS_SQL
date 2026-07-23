-- =============================================================================
-- HANDS-ON 2 - TASK 3: MULTI-TABLE RELATIONAL JOINS (04_join_queries.sql)
-- Demonstrates INNER JOIN, 3-Table JOIN, and LEFT JOIN missing relationships
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 25: List student's full name alongside department name (2-Table INNER JOIN)
-- -----------------------------------------------------------------------------
SELECT 
    s.student_id, 
    CONCAT(s.first_name, ' ', s.last_name) AS student_full_name, 
    d.dept_name AS major_department 
FROM 
    students s 
INNER JOIN 
    departments d ON s.department_id = d.department_id 
ORDER BY 
    d.dept_name, s.last_name;


-- -----------------------------------------------------------------------------
-- Step 26: Show enrollment details with student full name & course name (3-Table JOIN)
-- -----------------------------------------------------------------------------
SELECT 
    e.enrollment_id, 
    CONCAT(s.first_name, ' ', s.last_name) AS student_full_name, 
    c.course_code, 
    c.course_name, 
    e.enrollment_date, 
    COALESCE(e.grade, 'NOT EVALUATED') AS grade 
FROM 
    enrollments e 
INNER JOIN 
    students s ON e.student_id = s.student_id 
INNER JOIN 
    courses c ON e.course_id = c.course_id 
ORDER BY 
    c.course_code, s.last_name;


-- -----------------------------------------------------------------------------
-- Step 27: Find students who are NOT enrolled in any course (LEFT JOIN ... WHERE IS NULL)
-- -----------------------------------------------------------------------------
SELECT 
    s.student_id, 
    CONCAT(s.first_name, ' ', s.last_name) AS unenrolled_student_name, 
    s.email, 
    d.dept_name 
FROM 
    students s 
INNER JOIN 
    departments d ON s.department_id = d.department_id 
LEFT JOIN 
    enrollments e ON s.student_id = e.student_id 
WHERE 
    e.enrollment_id IS NULL 
ORDER BY 
    s.student_id;


-- -----------------------------------------------------------------------------
-- Step 28: Display every course with enrollment count (Include courses with 0 enrollments)
-- -----------------------------------------------------------------------------
SELECT 
    c.course_id, 
    c.course_code, 
    c.course_name, 
    COUNT(e.enrollment_id) AS total_enrolled_students 
FROM 
    courses c 
LEFT JOIN 
    enrollments e ON c.course_id = e.course_id 
GROUP BY 
    c.course_id, c.course_code, c.course_name 
ORDER BY 
    total_enrolled_students DESC, c.course_code ASC;


-- -----------------------------------------------------------------------------
-- Step 29: List each department with its professors (Include departments without professors)
-- -----------------------------------------------------------------------------
SELECT 
    d.dept_name, 
    d.head_of_dept, 
    COALESCE(p.prof_name, 'NO FACULTY ASSIGNED') AS professor_name, 
    COALESCE(p.salary, 0.00) AS salary 
FROM 
    departments d 
LEFT JOIN 
    professors p ON d.department_id = p.department_id 
ORDER BY 
    d.dept_name, p.prof_name;
