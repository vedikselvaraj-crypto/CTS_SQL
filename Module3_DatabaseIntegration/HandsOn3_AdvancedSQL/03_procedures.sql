-- =============================================================================
-- HANDS-ON 3 - TASK 3: STORED PROCEDURES & PL/PGSQL FUNCTIONS (03_procedures.sql)
-- Complete implementation for both PostgreSQL and MySQL
-- =============================================================================

-- Create Audit Log Table for Department Transfers
CREATE TABLE IF NOT EXISTS department_transfer_log (
    log_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    old_department_id INT NOT NULL,
    new_department_id INT NOT NULL,
    transferred_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- =============================================================================
-- SECTION 1: POSTGRESQL PL/PGSQL PROCEDURES & FUNCTIONS
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Step 44 (PostgreSQL): Function fn_enroll_student
-- Checks for duplicate enrollment and inserts record; raises error if duplicate.
-- -----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_enroll_student(
    p_student_id INT,
    p_course_id INT,
    p_enrollment_date DATE DEFAULT CURRENT_DATE
) 
RETURNS VOID 
LANGUAGE plpgsql 
AS $$
DECLARE
    v_exists INT;
BEGIN
    -- Check if duplicate enrollment exists
    SELECT COUNT(*) INTO v_exists 
    FROM enrollments 
    WHERE student_id = p_student_id AND course_id = p_course_id;

    IF v_exists > 0 THEN
        RAISE EXCEPTION 'DUPLICATE ENROLLMENT: Student % is already enrolled in course %', p_student_id, p_course_id;
    END IF;

    -- Insert new enrollment record
    INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
    VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);

    RAISE NOTICE 'SUCCESS: Enrolled student % into course %', p_student_id, p_course_id;
END;
$$;


-- -----------------------------------------------------------------------------
-- Step 45 & 46 (PostgreSQL): Procedure sp_transfer_student
-- Transactional department transfer with audit logging and rollback handling
-- -----------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE sp_transfer_student(
    p_student_id INT,
    p_new_dept_id INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_old_dept_id INT;
BEGIN
    -- Retrieve current department ID
    SELECT department_id INTO v_old_dept_id 
    FROM students 
    WHERE student_id = p_student_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'STUDENT_NOT_FOUND: Student ID % does not exist', p_student_id;
    END IF;

    -- Update Student Department
    UPDATE students 
    SET department_id = p_new_dept_id 
    WHERE student_id = p_student_id;

    -- Insert Audit Log
    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
    VALUES (p_student_id, v_old_dept_id, p_new_dept_id);

    RAISE NOTICE 'SUCCESS: Transferred student % from department % to %', p_student_id, v_old_dept_id, p_new_dept_id;

EXCEPTION
    WHEN OTHERS THEN
        -- Automatic Rollback occurs on exception in PL/pgSQL procedure block
        RAISE NOTICE 'TRANSACTION ROLLED BACK: Failure during department transfer: %', SQLERRM;
        RAISE;
END;
$$;


-- =============================================================================
-- SECTION 2: MYSQL EQUIVALENT STORED PROCEDURES (DELIMITER Syntax)
-- =============================================================================
/*
DELIMITER $$

-- Step 44 (MySQL): Stored Procedure sp_enroll_student
CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    DECLARE v_exists INT DEFAULT 0;

    SELECT COUNT(*) INTO v_exists 
    FROM enrollments 
    WHERE student_id = p_student_id AND course_id = p_course_id;

    IF v_exists > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'DUPLICATE ENROLLMENT ERROR';
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
    END IF;
END $$


-- Step 45 & 46 (MySQL): Stored Procedure sp_transfer_student
CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_dept_id INT
)
BEGIN
    DECLARE v_old_dept_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback on any SQL Exception
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    SELECT department_id INTO v_old_dept_id 
    FROM students 
    WHERE student_id = p_student_id;

    UPDATE students SET department_id = p_new_dept_id WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
    VALUES (p_student_id, v_old_dept_id, p_new_dept_id);

    COMMIT;
END $$

DELIMITER ;
*/
