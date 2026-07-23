"""
================================================================================
HANDS-ON 4 - TASK 3: N+1 QUERY PERFORMANCE BENCHMARK (n_plus_one.py)
================================================================================
Demonstrates the N+1 problem performance anti-pattern vs. optimized SQL JOIN.
Uses SQLite in-memory database to provide self-contained, reproducible execution.

Usage:
  python n_plus_one.py
================================================================================
"""

import sqlite3
import time
from typing import List, Tuple, Dict, Any


def create_in_memory_db() -> sqlite3.Connection:
    """Creates an in-memory SQLite database and populates sample dataset."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER NOT NULL,
            course_code TEXT NOT NULL,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """)

    # Seed 12 Enrollments across 5 Students
    students_data = [
        (1, 'Arjun', 'Mehta', 'arjun@college.edu'),
        (2, 'Priya', 'Suresh', 'priya@college.edu'),
        (3, 'Rohan', 'Verma', 'rohan@college.edu'),
        (4, 'Sneha', 'Patel', 'sneha@college.edu'),
        (5, 'Vikram', 'Das', 'vikram@college.edu')
    ]
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students_data)

    enrollments_data = [
        (1, 1, 'CS101', 'A'), (2, 1, 'CS102', 'B'),
        (3, 2, 'CS101', 'B'), (4, 2, 'CS103', 'A'),
        (5, 3, 'EC101', 'A'), (6, 4, 'ME101', 'B'),
        (7, 5, 'CS101', 'C'), (8, 5, 'CS102', 'A'),
        (9, 1, 'CS103', 'A'), (10, 2, 'EC101', 'B'),
        (11, 3, 'CS102', 'A'), (12, 4, 'CS101', 'B')
    ]
    cursor.executemany("INSERT INTO enrollments VALUES (?, ?, ?, ?)", enrollments_data)
    conn.commit()
    return conn


def simulate_n_plus_one_bad(conn: sqlite3.Connection) -> Tuple[List[Dict[str, Any]], int, float]:
    """APPROACH 1: BAD N+1 LAZY LOADING
    - Issue 1 query to fetch N enrollment rows.
    - Loop over N rows and issue N separate queries to fetch student names.
    - Total Queries Issued: N + 1 (12 + 1 = 13 queries).
    """
    cursor = conn.cursor()
    query_count = 0
    start_time = time.time()

    # Query 1: Fetch all N enrollments
    cursor.execute("SELECT enrollment_id, student_id, course_code, grade FROM enrollments")
    query_count += 1
    enrollments = cursor.fetchall()

    results = []
    # Loop over N rows -> Issues N additional database queries!
    for enr in enrollments:
        enr_id, stud_id, c_code, grade = enr
        
        # Query 2..N+1: Fetch student name for each row
        cursor.execute("SELECT first_name, last_name FROM students WHERE student_id = ?", (stud_id,))
        query_count += 1
        student = cursor.fetchone()
        
        results.append({
            "enrollment_id": enr_id,
            "student_name": f"{student[0]} {student[1]}",
            "course_code": c_code,
            "grade": grade
        })

    elapsed_time = time.time() - start_time
    return results, query_count, elapsed_time


def simulate_eager_join_good(conn: sqlite3.Connection) -> Tuple[List[Dict[str, Any]], int, float]:
    """APPROACH 2: OPTIMIZED EAGER JOIN
    - Issue 1 single SQL JOIN query retrieving enrollment and student name data.
    - Total Queries Issued: 1 query.
    """
    cursor = conn.cursor()
    query_count = 0
    start_time = time.time()

    # Query 1: Single SQL JOIN
    cursor.execute("""
        SELECT 
            e.enrollment_id, 
            s.first_name || ' ' || s.last_name AS student_name, 
            e.course_code, 
            e.grade 
        FROM 
            enrollments e 
        JOIN 
            students s ON e.student_id = s.student_id
    """)
    query_count += 1
    rows = cursor.fetchall()

    results = [
        {
            "enrollment_id": r[0],
            "student_name": r[1],
            "course_code": r[2],
            "grade": r[3]
        }
        for r in rows
    ]

    elapsed_time = time.time() - start_time
    return results, query_count, elapsed_time


"""
================================================================================
REAL-WORLD SCENARIO ANALYSIS (10,000 ENROLLMENT RECORDS):
--------------------------------------------------------------------------------
Question: In a production web application with 10,000 enrollment records, how 
many extra database round-trips would the N+1 lazy loading approach issue?

Answer:
- Total Queries Issued by Bad N+1 Approach: 1 + 10,000 = 10,001 database queries!
- Total Queries Issued by Eager JOIN Approach: 1 single database query.
- Impact: The N+1 approach issues 10,000 EXTRA unnecessary database network round-trips.
  If network latency is 2ms per query, N+1 adds 20 SECONDS of artificial delay 
  and saturates the database connection pool, leading to application downtime.
================================================================================
"""

if __name__ == "__main__":
    connection = create_in_memory_db()

    print("[INFO] Executing Approach 1 (Bad N+1 Lazy Loading)...")
    res1, count1, time1 = simulate_n_plus_one_bad(connection)

    print("[INFO] Executing Approach 2 (Optimized SQL JOIN Eager Loading)...")
    res2, count2, time2 = simulate_eager_join_good(connection)

    print("\n================================================================================")
    print("N+1 QUERY BENCHMARK RESULTS")
    print("================================================================================")
    print(f"Approach 1 (Bad N+1 Lazy Loading): {count1} database round-trips | Execution Time: {time1:.6f}s")
    print(f"Approach 2 (Optimized Eager JOIN):  {count2} database round-trip  | Execution Time: {time2:.6f}s")
    print("--------------------------------------------------------------------------------")
    
    speedup = (time1 / time2) if time2 > 0 else 1.0
    queries_saved = count1 - count2
    print(f"Performance Gain: Approach 2 was {speedup:.2f}x FASTER and saved {queries_saved} database queries!")
    print("================================================================================\n")
    
    assert res1 == res2, "Data mismatch between approaches!"
    print("[SUCCESS] Data consistency verified across both approaches.")
