-- =============================================================================
-- HANDS-ON 2 - TASK 2: SINGLE-TABLE FILTERING & SELECTION (03_select_queries.sql)
-- Demonstrates WHERE, ORDER BY, BETWEEN, LIKE, and simple GROUP BY
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 20: Retrieve all students enrolled in 2022, ordered by last_name alphabetically
-- -----------------------------------------------------------------------------
SELECT 
    student_id, 
    first_name, 
    last_name, 
    email, 
    enrollment_year 
FROM 
    students 
WHERE 
    enrollment_year = 2022 
ORDER BY 
    last_name ASC, 
    first_name ASC;


-- -----------------------------------------------------------------------------
-- Step 21: Find all courses with more than 3 credits, sorted by credits descending
-- -----------------------------------------------------------------------------
SELECT 
    course_id, 
    course_code, 
    course_name, 
    credits 
FROM 
    courses 
WHERE 
    credits > 3 
ORDER BY 
    credits DESC, 
    course_code ASC;


-- -----------------------------------------------------------------------------
-- Step 22: List all professors whose salary is between 80,000 and 95,000
-- Note: BETWEEN operator is inclusive on both lower and upper bounds
-- -----------------------------------------------------------------------------
SELECT 
    professor_id, 
    prof_name, 
    email, 
    salary 
FROM 
    professors 
WHERE 
    salary BETWEEN 80000.00 AND 95000.00 
ORDER BY 
    salary DESC;


-- -----------------------------------------------------------------------------
-- Step 23: Find all students whose email ends with '@college.edu' using LIKE
-- -----------------------------------------------------------------------------
SELECT 
    student_id, 
    first_name, 
    last_name, 
    email 
FROM 
    students 
WHERE 
    email LIKE '%@college.edu' 
ORDER BY 
    student_id ASC;


-- -----------------------------------------------------------------------------
-- Step 24: Count the total number of students per enrollment_year
-- -----------------------------------------------------------------------------
SELECT 
    enrollment_year, 
    COUNT(*) AS total_students 
FROM 
    students 
GROUP BY 
    enrollment_year 
ORDER BY 
    enrollment_year ASC;
