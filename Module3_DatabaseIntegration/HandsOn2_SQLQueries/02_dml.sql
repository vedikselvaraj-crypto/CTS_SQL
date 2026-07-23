-- =============================================================================
-- HANDS-ON 2 - TASK 1: DML MUTATIONS & VERIFICATION (02_dml.sql)
-- Executes UPDATE, DELETE, and verification COUNT queries
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 17: Update grade of student_id = 5 for course_id = 1 from 'C' to 'B'
-- -----------------------------------------------------------------------------
-- Preview row before update
SELECT student_id, course_id, grade 
FROM enrollments 
WHERE student_id = 5 AND course_id = 1;

-- Execute UPDATE statement
UPDATE enrollments 
SET grade = 'B' 
WHERE student_id = 5 AND course_id = 1;

-- Verify UPDATE execution
SELECT student_id, course_id, grade 
FROM enrollments 
WHERE student_id = 5 AND course_id = 1;


-- -----------------------------------------------------------------------------
-- Step 18: Delete enrollments where grade IS NULL (unevaluated enrollments)
-- -----------------------------------------------------------------------------
-- Preview rows to be deleted (Students 4 and 7 enrolled in Thermodynamics)
SELECT enrollment_id, student_id, course_id, grade 
FROM enrollments 
WHERE grade IS NULL;

-- Execute DELETE statement
DELETE FROM enrollments 
WHERE grade IS NULL;


-- -----------------------------------------------------------------------------
-- Step 19: Verify row counts using SELECT COUNT(*) after operations
-- -----------------------------------------------------------------------------
SELECT 'students_total' AS metric, COUNT(*) AS row_count FROM students
UNION ALL
SELECT 'enrollments_active', COUNT(*) FROM enrollments
UNION ALL
SELECT 'enrollments_null_grade', COUNT(*) FROM enrollments WHERE grade IS NULL;
