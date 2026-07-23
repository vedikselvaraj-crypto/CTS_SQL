-- =============================================================================
-- HANDS-ON 3 - TASK 1: ADVANCED SUBQUERIES SCRIPT (01_subqueries.sql)
-- Non-correlated, Correlated, NOT EXISTS, and Derived Tables
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 35: Find students enrolled in more courses than the average enrollments per student
-- (Uses non-correlated subquery to calculate overall average course count)
-- -----------------------------------------------------------------------------
WITH student_course_counts AS (
    SELECT student_id, COUNT(course_id) AS course_count
    FROM enrollments
    GROUP BY student_id
)
SELECT 
    s.student_id, 
    CONCAT(s.first_name, ' ', s.last_name) AS student_name, 
    s.email, 
    scc.course_count 
FROM 
    students s 
INNER JOIN 
    student_course_counts scc ON s.student_id = scc.student_id 
WHERE 
    scc.course_count > (
        -- Non-correlated Subquery: Average enrollments per student across whole college
        SELECT AVG(cnt.course_count) 
        FROM (
            SELECT COUNT(course_id) AS course_count 
            FROM enrollments 
            GROUP BY student_id
        ) cnt
    )
ORDER BY 
    scc.course_count DESC, s.last_name;


-- -----------------------------------------------------------------------------
-- Step 36: List courses in which ALL enrolled students received a grade of 'A'
-- (Uses Correlated Subquery with NOT EXISTS)
-- -----------------------------------------------------------------------------
SELECT 
    c.course_id, 
    c.course_code, 
    c.course_name 
FROM 
    courses c 
WHERE 
    EXISTS (
        SELECT 1 FROM enrollments e WHERE e.course_id = c.course_id
    )
    AND NOT EXISTS (
        -- Correlated Subquery: Find any enrollment for this course with a grade OTHER than 'A'
        SELECT 1 
        FROM enrollments e2 
        WHERE e2.course_id = c.course_id 
          AND (e2.grade <> 'A' OR e2.grade IS NULL)
    )
ORDER BY 
    c.course_code;


-- -----------------------------------------------------------------------------
-- Step 37: Find professor with the highest salary in each department
-- (Uses Correlated Subquery referencing outer department_id)
-- -----------------------------------------------------------------------------
SELECT 
    p1.professor_id, 
    p1.prof_name, 
    d.dept_name, 
    p1.salary 
FROM 
    professors p1 
INNER JOIN 
    departments d ON p1.department_id = d.department_id 
WHERE 
    p1.salary = (
        -- Correlated Subquery: Maximum salary for p1's department
        SELECT MAX(p2.salary) 
        FROM professors p2 
        WHERE p2.department_id = p1.department_id
    )
ORDER BY 
    p1.salary DESC;


-- -----------------------------------------------------------------------------
-- Step 38: Derived Table in FROM clause: Per-department avg salary exceeding 85,000
-- -----------------------------------------------------------------------------
SELECT 
    dept_summary.dept_name, 
    dept_summary.total_professors, 
    ROUND(dept_summary.avg_salary, 2) AS average_salary 
FROM (
    -- Derived Table Subquery in FROM clause
    SELECT 
        d.dept_name, 
        COUNT(p.professor_id) AS total_professors, 
        AVG(p.salary) AS avg_salary 
    FROM 
        departments d 
    INNER JOIN 
        professors p ON d.department_id = p.department_id 
    GROUP BY 
        d.department_id, d.dept_name
) AS dept_summary 
WHERE 
    dept_summary.avg_salary > 85000.00 
ORDER BY 
    average_salary DESC;
