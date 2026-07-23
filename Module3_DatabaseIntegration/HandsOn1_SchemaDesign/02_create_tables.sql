-- =============================================================================
-- HANDS-ON 1: TABLE CREATION DDL SCRIPT (02_create_tables.sql)
-- Target System: Student Course Registration System (college_db)
-- PostgreSQL Dialect with MySQL Dual Syntax Documentation
-- =============================================================================

-- Clean existing tables if present (Ordered to respect Foreign Key dependency hierarchy)
DROP TABLE IF EXISTS enrollments CASCADE;
DROP TABLE IF EXISTS professors CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS departments CASCADE;

-- -----------------------------------------------------------------------------
-- 1. TABLE: departments
-- Primary lookup entity for college academic divisions
-- -----------------------------------------------------------------------------
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,                     -- PostgreSQL SERIAL (MySQL: INT AUTO_INCREMENT PRIMARY KEY)
    dept_name VARCHAR(100) NOT NULL UNIQUE,                -- Department title
    hod_name VARCHAR(100) NOT NULL,                        -- Head of Department
    budget DECIMAL(12, 2) NOT NULL DEFAULT 0.00            -- Annual operating budget
);

-- -----------------------------------------------------------------------------
-- 2. TABLE: students
-- Enrolled student entity referencing major department
-- -----------------------------------------------------------------------------
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,                        -- Unique Student Identifier
    first_name VARCHAR(50) NOT NULL,                       -- Given name
    last_name VARCHAR(50) NOT NULL,                        -- Surname
    email VARCHAR(100) NOT NULL UNIQUE,                    -- College institutional email
    date_of_birth DATE NOT NULL,                           -- Birthdate
    department_id INT NOT NULL,                            -- Foreign Key to departments
    enrollment_year INT NOT NULL DEFAULT 2026,             -- Year admitted
    CONSTRAINT fk_students_department 
        FOREIGN KEY (department_id) 
        REFERENCES departments(department_id) 
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
);

-- -----------------------------------------------------------------------------
-- 3. TABLE: courses
-- Academic course catalog offerings
-- -----------------------------------------------------------------------------
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,                         -- Unique Course Primary Key
    course_name VARCHAR(150) NOT NULL,                     -- Title of course
    course_code VARCHAR(20) NOT NULL UNIQUE,               -- Unique catalog code (e.g. CS101)
    credits INT NOT NULL DEFAULT 3,                        -- Credit value
    department_id INT NOT NULL,                            -- Department offering course
    CONSTRAINT fk_courses_department 
        FOREIGN KEY (department_id) 
        REFERENCES departments(department_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- -----------------------------------------------------------------------------
-- 4. TABLE: enrollments
-- Junction table mapping many-to-many relationship between students & courses
-- -----------------------------------------------------------------------------
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,                      -- Unique enrollment record ID
    student_id INT NOT NULL,                               -- Foreign Key to student
    course_id INT NOT NULL,                                -- Foreign Key to course
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,    -- Date registered
    grade CHAR(2) NULL,                                    -- Letter grade (A, B, C, D, F, or NULL)
    CONSTRAINT fk_enrollments_student 
        FOREIGN KEY (student_id) 
        REFERENCES students(student_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    CONSTRAINT fk_enrollments_course 
        FOREIGN KEY (course_id) 
        REFERENCES courses(course_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- -----------------------------------------------------------------------------
-- 5. TABLE: professors
-- Academic faculty staff entity
-- -----------------------------------------------------------------------------
CREATE TABLE professors (
    professor_id SERIAL PRIMARY KEY,                      -- Unique Faculty ID
    prof_name VARCHAR(100) NOT NULL,                       -- Professor full name
    email VARCHAR(100) NOT NULL UNIQUE,                    -- Faculty email
    department_id INT NOT NULL,                            -- Primary department assignment
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0.00,           -- Annual base compensation
    CONSTRAINT fk_professors_department 
        FOREIGN KEY (department_id) 
        REFERENCES departments(department_id) 
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
);

-- =============================================================================
-- MYSQL EQUIVALENT DDL SYNTAX REFERENCE:
-- =============================================================================
/*
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    hod_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12, 2) NOT NULL DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL,
    department_id INT NOT NULL,
    enrollment_year INT NOT NULL DEFAULT 2026,
    CONSTRAINT fk_students_department FOREIGN KEY (department_id) REFERENCES departments(department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) NOT NULL UNIQUE,
    credits INT NOT NULL DEFAULT 3,
    department_id INT NOT NULL,
    CONSTRAINT fk_courses_department FOREIGN KEY (department_id) REFERENCES departments(department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    grade CHAR(2) NULL,
    CONSTRAINT fk_enrollments_student FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department_id INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    CONSTRAINT fk_professors_department FOREIGN KEY (department_id) REFERENCES departments(department_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
*/
