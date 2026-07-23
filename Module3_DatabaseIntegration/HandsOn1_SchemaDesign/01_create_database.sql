-- =============================================================================
-- HANDS-ON 1: DATABASE CREATION SCRIPT (01_create_database.sql)
-- Target System: Student Course Registration System (college_db)
-- =============================================================================

-- -----------------------------------------------------------------------------
-- POSTGRESQL DIALECT
-- -----------------------------------------------------------------------------
-- Drop database if exists to ensure clean execution environment
DROP DATABASE IF EXISTS college_db;

-- Create college_db database
CREATE DATABASE college_db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE college_db IS 'Database for Digital Nurture 5.0 Student Course Registration System';

-- Connect to target database (psql specific)
\c college_db;


-- -----------------------------------------------------------------------------
-- MYSQL EQUIVALENT DIALECT (Commented for reference)
-- -----------------------------------------------------------------------------
/*
DROP DATABASE IF EXISTS college_db;
CREATE DATABASE college_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE college_db;
*/
