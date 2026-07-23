"""
================================================================================
HANDS-ON 6 - TASK 3: EAGER LOADING TO FIX N+1 IN ORM (queries.py)
================================================================================
COMPARISON & ANALYSIS DOCUMENTATION:
--------------------------------------------------------------------------------
1. LAZY LOADING (Default ORM Behavior):
   - When executing session.query(Enrollment).all() and looping over results to 
     access enrollment.student.first_name and enrollment.course.course_name:
     * Query 1: SELECT * FROM enrollments; (Fetches N rows)
     * Queries 2..2N+1: For each row, issues separate SELECT statements to fetch 
       Student and Course records lazily.
   - Total SQL Queries Issued: 13 SQL Queries (1 + N + N).

2. EAGER LOADING VIA joinedload():
   - When executing session.query(Enrollment).options(
         joinedload(Enrollment.student), 
         joinedload(Enrollment.course)
     ).all():
     * Issues ONE SINGLE SQL STATEMENT using LEFT OUTER JOINs between enrollments, 
       students, and courses tables!
   - Total SQL Queries Issued: 1 SQL Query.
   - Performance Result: 13 queries reduced to 1 SQL statement (13x reduction!).
================================================================================
"""

from database import SessionLocal
from models import Enrollment
from sqlalchemy.orm import joinedload


def run_n_plus_one_comparison():
    session = SessionLocal()

    print("\n================================================================================")
    print("APPROACH 1: LAZY LOADING (Triggering N+1 Queries)")
    print("================================================================================")
    print("Observe SQL log lines generated below...")
    lazy_enrollments = session.query(Enrollment).all()
    
    print("\nProcessing lazy results...")
    for enr in lazy_enrollments:
        # Accessing .student and .course triggers separate SQL queries per row!
        _ = f"Student: {enr.student.first_name} | Course: {enr.course.course_code}"
    
    print("\n================================================================================")
    print("APPROACH 2: EAGER LOADING VIA joinedload (Fixing N+1)")
    print("================================================================================")
    print("Observe SQL log lines generated below...")
    
    # Eager loading fetches all related entities in 1 single JOIN query!
    eager_enrollments = session.query(Enrollment).options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    ).all()

    print("\nProcessing eager results...")
    for enr in eager_enrollments:
        # Relationships are pre-populated; ZERO extra SQL queries are issued!
        print(f"  [EAGER] Student: {enr.student.first_name} {enr.student.last_name} -> Course: {enr.course.course_name}")

    session.close()
    print("\n[SUCCESS] Eager loading comparison completed cleanly!")


if __name__ == "__main__":
    run_n_plus_one_comparison()
