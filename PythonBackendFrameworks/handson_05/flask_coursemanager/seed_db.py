"""
================================================================================
FLASK DATABASE SEEDING SCRIPT (seed_db.py)
================================================================================
"""

from app import create_app
from database import db
from models import Department, Course, Student, Enrollment

app = create_app()

with app.app_context():
    print("[INFO] Recreating database tables...")
    db.drop_all()
    db.create_all()

    print("[INFO] Inserting sample departments...")
    cs_dept = Department(name="Computer Science", head_of_dept="Dr. Alan Turing", budget=500000.0)
    ee_dept = Department(name="Electrical Engineering", head_of_dept="Dr. Nikola Tesla", budget=450000.0)
    db.session.add_all([cs_dept, ee_dept])
    db.session.commit()

    print("[INFO] Inserting sample courses...")
    c1 = Course(name="Intro to Programming", code="CS-101", credits=3, department_id=cs_dept.id)
    c2 = Course(name="Data Structures & Algorithms", code="CS-201", credits=4, department_id=cs_dept.id)
    c3 = Course(name="Circuit Analysis", code="EE-101", credits=3, department_id=ee_dept.id)
    db.session.add_all([c1, c2, c3])
    db.session.commit()

    print("[INFO] Inserting sample students...")
    s1 = Student(first_name="Alice", last_name="Smith", email="alice@college.edu", department_id=cs_dept.id, enrollment_year=2024)
    s2 = Student(first_name="Bob", last_name="Jones", email="bob@college.edu", department_id=cs_dept.id, enrollment_year=2025)
    db.session.add_all([s1, s2])
    db.session.commit()

    print("[INFO] Inserting sample enrollments...")
    e1 = Enrollment(student_id=s1.id, course_id=c1.id, grade="A")
    e2 = Enrollment(student_id=s1.id, course_id=c2.id, grade="A-")
    e3 = Enrollment(student_id=s2.id, course_id=c1.id, grade="B+")
    db.session.add_all([e1, e2, e3])
    db.session.commit()

    print("[SUCCESS] Database seeded successfully with departments, courses, students, and enrollments!")
