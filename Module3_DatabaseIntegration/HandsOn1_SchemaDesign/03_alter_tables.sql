-- =============================================================================
-- HANDS-ON 1 - TASK 3: ALTER AND EXTEND SCHEMA DDL SCRIPT (03_alter_tables.sql)
-- Safe schema evolution without data loss
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 10: Add phone_number column to students table
-- -----------------------------------------------------------------------------
ALTER TABLE students 
ADD COLUMN phone_number VARCHAR(15) NULL;

-- Verify addition (Comment)
-- SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students';


-- -----------------------------------------------------------------------------
-- Step 11: Add max_seats column with default value 60 to courses table
-- -----------------------------------------------------------------------------
ALTER TABLE courses 
ADD COLUMN max_seats INT NOT NULL DEFAULT 60;


-- -----------------------------------------------------------------------------
-- Step 12: Add CHECK constraint to enrollments table ensuring valid letter grade
-- Enforces allowed domain values: ('A', 'B', 'C', 'D', 'F') or NULL
-- -----------------------------------------------------------------------------
ALTER TABLE enrollments 
ADD CONSTRAINT chk_enrollments_grade 
CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL);


-- -----------------------------------------------------------------------------
-- Step 13: Rename column hod_name in departments to head_of_dept
-- -----------------------------------------------------------------------------
-- PostgreSQL Syntax:
ALTER TABLE departments 
RENAME COLUMN hod_name TO head_of_dept;

-- MySQL 8.0+ Equivalent Syntax:
-- ALTER TABLE departments RENAME COLUMN hod_name TO head_of_dept;
-- MySQL 5.7 Legacy Syntax:
-- ALTER TABLE departments CHANGE hod_name head_of_dept VARCHAR(100) NOT NULL;


-- -----------------------------------------------------------------------------
-- Step 14: Drop phone_number column from students (Simulate schema rollback)
-- -----------------------------------------------------------------------------
ALTER TABLE students 
DROP COLUMN phone_number;


-- =============================================================================
-- VERIFICATION QUERY
-- =============================================================================
SELECT 
    table_name, 
    column_name, 
    data_type, 
    is_nullable 
FROM 
    information_schema.columns 
WHERE 
    table_schema = 'public' 
    AND table_name IN ('departments', 'students', 'courses', 'enrollments', 'professors')
ORDER BY 
    table_name, ordinal_position;
