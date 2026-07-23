-- =============================================================================
-- HANDS-ON 3 - TASK 4: ACID TRANSACTIONS & SAVEPOINT WORKFLOW (04_transactions.sql)
-- Demonstrates BEGIN, SAVEPOINT, partial ROLLBACK TO SAVEPOINT, and COMMIT
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 47: Transactional SAVEPOINT Checkpoint Demonstration
-- -----------------------------------------------------------------------------

-- Preview initial enrollments count
SELECT COUNT(*) AS initial_enrollment_count FROM enrollments;

-- 1. Begin Explicit Transaction Block
BEGIN TRANSACTION;

-- 2. Insert First Valid Enrollment Record (Student 2 into Course 4 - Circuit Theory)
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (2, 4, CURRENT_DATE, 'A');

-- 3. Create Mid-Transaction Checkpoint
SAVEPOINT savepoint_first_insert;

-- 4. Attempt Second Deliberately Failing Insert (Invalid Foreign Key course_id = 9999)
-- In a script runner block, we catch the failure and trigger rollback to savepoint:
DO $$
BEGIN
    INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
    VALUES (2, 9999, CURRENT_DATE, 'F');
EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE 'Caught deliberate foreign key failure! Rolling back to savepoint_first_insert...';
    -- Rollback to mid-transaction checkpoint, keeping the first insert intact
    -- Note: In standard SQL execution: ROLLBACK TO SAVEPOINT savepoint_first_insert;
END;
$$;

-- 5. Commit Transaction (Persists the first valid insert)
COMMIT;


-- -----------------------------------------------------------------------------
-- VERIFICATION OF SAVEPOINT PARTIAL ROLLBACK RESULT
-- -----------------------------------------------------------------------------
-- Verify that Student 2 enrollment in Course 4 was saved, while invalid course 9999 was not.
SELECT 
    enrollment_id, 
    student_id, 
    course_id, 
    enrollment_date, 
    grade 
FROM 
    enrollments 
WHERE 
    student_id = 2 AND course_id = 4;

-- Total enrollments count verification
SELECT COUNT(*) AS final_enrollment_count FROM enrollments;
