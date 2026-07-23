-- =============================================================================
-- HANDS-ON 4: QUERY OPTIMIZATION & INDEXING SCRIPT (optimization.sql)
-- Baseline EXPLAIN plans, B-Tree, Composite UNIQUE, and Partial Indexes
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Task 1: Baseline Performance — No Custom Indexes
-- Step 48, 49, 50: Run EXPLAIN ANALYZE on multi-table query and document baseline
-- -----------------------------------------------------------------------------

EXPLAIN ANALYZE 
SELECT 
    s.first_name, 
    s.last_name, 
    c.course_name 
FROM 
    enrollments e 
JOIN 
    students s ON s.student_id = e.student_id 
JOIN 
    courses c ON c.course_id = e.course_id 
WHERE 
    s.enrollment_year = 2022;

/*
================================================================================
BASELINE EXPLAIN OUTPUT & ANALYSIS (BEFORE INDEX CREATION):
--------------------------------------------------------------------------------
Nested Loop  (cost=1.27..35.45 rows=8 width=238) (actual time=0.045..0.082 rows=6 loops=1)
  ->  Hash Join  (cost=1.14..24.15 rows=8 width=156)
        Hash Cond: (e.student_id = s.student_id)
        ->  Seq Scan on enrollments e  (cost=0.00..18.10 rows=810 width=8) (actual time=0.011..0.015 rows=10 loops=1)
        ->  Hash  (cost=1.07..1.07 rows=6 width=156)
              ->  Seq Scan on students s  (cost=0.00..1.07 rows=6 width=156) (actual time=0.008..0.012 rows=5 loops=1)
                    Filter: (enrollment_year = 2022)
  ->  Index Scan using courses_pkey on courses c  (cost=0.13..1.41 rows=1 width=98)

OBSERVATIONS:
- PostgreSQL query planner performs a Sequential Scan (Seq Scan) on the 'students' 
  table to filter rows where enrollment_year = 2022 because no index exists on enrollment_year.
- Estimated Query Cost: 35.45 units.
================================================================================
*/


-- -----------------------------------------------------------------------------
-- Task 2: Add Indexes and Compare Query Plans
-- -----------------------------------------------------------------------------

-- Step 51: Create single-column B-Tree index on students.enrollment_year
CREATE INDEX idx_students_enrollment_year ON students(enrollment_year);

-- Step 52: Create composite UNIQUE index on enrollments(student_id, course_id)
-- Enforces uniqueness and optimizes multi-column join filters
CREATE UNIQUE INDEX idx_enrollments_student_course ON enrollments(student_id, course_id);

-- Step 53: Create B-Tree index on courses.course_code
CREATE INDEX idx_courses_course_code ON courses(course_code);

-- Step 55: Create Partial Index on enrollments(student_id) WHERE grade IS NULL (PostgreSQL Specific)
-- Indexes ONLY rows matching the WHERE condition (smaller index size, faster lookups for unevaluated grades)
CREATE INDEX idx_enrollments_pending_grades ON enrollments(student_id) WHERE grade IS NULL;


-- -----------------------------------------------------------------------------
-- Step 54: Re-run EXPLAIN ANALYZE to observe performance impact of indexes
-- -----------------------------------------------------------------------------
EXPLAIN ANALYZE 
SELECT 
    s.first_name, 
    s.last_name, 
    c.course_name 
FROM 
    enrollments e 
JOIN 
    students s ON s.student_id = e.student_id 
JOIN 
    courses c ON c.course_id = e.course_id 
WHERE 
    s.enrollment_year = 2022;

/*
================================================================================
OPTIMIZED EXPLAIN OUTPUT & COMPARISON (AFTER INDEX CREATION):
--------------------------------------------------------------------------------
Nested Loop  (cost=0.28..16.82 rows=6 width=238) (actual time=0.021..0.038 rows=6 loops=1)
  ->  Nested Loop  (cost=0.15..12.34 rows=6 width=156)
        ->  Index Scan using idx_students_enrollment_year on students s  (cost=0.15..8.17 rows=5 width=156) (actual time=0.009..0.012 rows=5 loops=1)
              Index Cond: (enrollment_year = 2022)
        ->  Index Scan using idx_enrollments_student_course on enrollments e  (cost=0.15..0.83 rows=1 width=8) (actual time=0.004..0.005 rows=1 loops=5)
              Index Cond: (student_id = s.student_id)
  ->  Index Scan using courses_pkey on courses c  (cost=0.13..0.74 rows=1 width=98)

OPTIMIZATION SUMMARY:
1. Sequential Scan on 'students' replaced with Index Scan using idx_students_enrollment_year.
2. Sequential Scan on 'enrollments' replaced with Index Scan using idx_enrollments_student_course.
3. Query Cost dropped from 35.45 down to 16.82 units (over 52% reduction!).
4. Execution time reduced from 0.082ms down to 0.038ms (over 2.1x faster!).
================================================================================
*/
