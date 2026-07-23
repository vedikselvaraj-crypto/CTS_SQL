-- =============================================================================
-- HANDS-ON 2 - TASK 4: AGGREGATION & GROUPING QUERIES (05_aggregate_queries.sql)
-- Demonstrates COUNT, AVG, ROUND, SUM, MAX, GROUP BY, and HAVING
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 30: Calculate total number of enrollments per course
-- -----------------------------------------------------------------------------
SELECT 
    c.course_code, 
    c.course_name, 
    COUNT(e.enrollment_id) AS total_enrollment_count 
FROM 
    courses c 
LEFT JOIN 
    enrollments e ON c.course_id = e.course_id 
GROUP BY 
    c.course_id, c.course_code, c.course_name 
ORDER BY 
    total_enrollment_count DESC;


-- -----------------------------------------------------------------------------
-- Step 31: Find average salary of professors per department rounded to 2 decimals
-- -----------------------------------------------------------------------------
SELECT 
    d.dept_name, 
    COUNT(p.professor_id) AS total_professors, 
    ROUND(AVG(p.salary), 2) AS average_professor_salary 
FROM 
    departments d 
LEFT JOIN 
    professors p ON d.department_id = p.department_id 
GROUP BY 
    d.department_id, d.dept_name 
ORDER BY 
    average_professor_salary DESC;


-- -----------------------------------------------------------------------------
-- Step 32: Find all departments where total department budget exceeds 600,000
-- -----------------------------------------------------------------------------
SELECT 
    department_id, 
    dept_name, 
    head_of_dept, 
    budget 
FROM 
    departments 
WHERE 
    budget > 600000.00 
ORDER BY 
    budget DESC;


-- -----------------------------------------------------------------------------
-- Step 33: Grade distribution for course 'CS101' (Count of each grade A, B, C, D, F)
-- -----------------------------------------------------------------------------
SELECT 
    c.course_code, 
    COALESCE(e.grade, 'NO_GRADE') AS grade_letter, 
    COUNT(*) AS grade_count 
FROM 
    enrollments e 
INNER JOIN 
    courses c ON e.course_id = c.course_id 
WHERE 
    c.course_code = 'CS101' 
GROUP BY 
    c.course_code, e.grade 
ORDER BY 
    grade_letter ASC;


-- -----------------------------------------------------------------------------
-- Step 34: List departments where more than 2 students are enrolled (HAVING clause)
-- -----------------------------------------------------------------------------
SELECT 
    d.dept_name, 
    COUNT(DISTINCT s.student_id) AS enrolled_students_count 
FROM 
    departments d 
INNER JOIN 
    students s ON d.department_id = s.department_id 
INNER JOIN 
    enrollments e ON s.student_id = e.student_id 
GROUP BY 
    d.department_id, d.dept_name 
HAVING 
    COUNT(DISTINCT s.student_id) > 2 
ORDER BY 
    enrolled_students_count DESC;
