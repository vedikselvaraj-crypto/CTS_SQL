"""
================================================================================
HANDS-ON 2: DJANGO ORM QUERY DEMONSTRATION SCRIPT (shell_examples.py)
================================================================================
Executes CRUD operations, relation lookups, annotations, select_related JOINs,
and F() expressions directly using Django ORM.

Usage:
  python manage.py shell < shell_examples.py
================================================================================
"""

import os
import django

# Setup Django environment if executed standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')
django.setup()

from django.db.models import Count, F
from django.db import connection
from courses.models import Department, Course, Student, Enrollment


def run_orm_demonstration():
    print("\n=== STEP 16: CRUD Operations - Creating Records ===")
    # Clear existing data for clean execution
    Enrollment.objects.all().delete()
    Student.objects.all().delete()
    Course.objects.all().delete()
    Department.objects.all().delete()

    # Create 2 Departments
    cs_dept = Department.objects.create(name="Computer Science", head_of_dept="Dr. Alan Turing", budget=500000.00)
    ee_dept = Department.objects.create(name="Electrical Engineering", head_of_dept="Dr. Nikola Tesla", budget=450000.00)
    print(f"[CREATED] Departments: {cs_dept}, {ee_dept}")

    # Create 4 Courses
    c1 = Course.objects.create(name="Intro to Programming", code="CS-101", credits=3, department=cs_dept)
    c2 = Course.objects.create(name="Data Structures & Algorithms", code="CS-201", credits=4, department=cs_dept)
    c3 = Course.objects.create(name="Database Management Systems", code="CS-301", credits=4, department=cs_dept)
    c4 = Course.objects.create(name="Circuit Analysis", code="EE-101", credits=3, department=ee_dept)
    print(f"[CREATED] 4 Courses under {cs_dept.name} and {ee_dept.name}")

    # Create 5 Students
    s1 = Student.objects.create(first_name="Alice", last_name="Smith", email="alice@college.edu", department=cs_dept, enrollment_year=2024)
    s2 = Student.objects.create(first_name="Bob", last_name="Jones", email="bob@college.edu", department=cs_dept, enrollment_year=2024)
    s3 = Student.objects.create(first_name="Charlie", last_name="Brown", email="charlie@college.edu", department=cs_dept, enrollment_year=2025)
    s4 = Student.objects.create(first_name="Diana", last_name="Prince", email="diana@college.edu", department=ee_dept, enrollment_year=2024)
    s5 = Student.objects.create(first_name="Evan", last_name="Wright", email="evan@college.edu", department=cs_dept, enrollment_year=2026)
    print(f"[CREATED] 5 Students")

    # Create Enrollments
    e1 = Enrollment.objects.create(student=s1, course=c1, grade="A")
    e2 = Enrollment.objects.create(student=s1, course=c2, grade="A-")
    e3 = Enrollment.objects.create(student=s2, course=c1, grade="B+")
    e4 = Enrollment.objects.create(student=s4, course=c4, grade="A")
    print(f"[CREATED] 4 Enrollments")

    print("\n=== STEP 17: ForeignKey Lookup across Relationship ===")
    cs_courses = Course.objects.filter(department__name='Computer Science')
    print(f"Courses in Computer Science ({cs_courses.count()} found):")
    for crs in cs_courses:
        print(f"  - {crs.code}: {crs.name} ({crs.credits} credits)")

    print("\n=== STEP 18: Aggregation & Annotation (.annotate and Count) ===")
    dept_counts = Department.objects.annotate(course_count=Count('courses')).values('name', 'course_count')
    print("Course count per department:")
    for d in dept_counts:
        print(f"  - Department: {d['name']} | Total Courses: {d['course_count']}")

    print("\n=== STEP 19: Performance Optimization via select_related() ===")
    # Clear query log
    connection.queries_log.clear()
    students_with_dept = Student.objects.select_related('department').all()
    print("Fetching all students along with their department in a single SQL JOIN query:")
    for st in students_with_dept:
        print(f"  - {st.first_name} {st.last_name} | Major: {st.department.name}")
    print(f"[SQL QUERIES EXECUTED]: {len(connection.queries)} query executed!")

    print("\n=== STEP 20: Atomic Database Update using F() Expressions ===")
    print("Original Budgets:")
    for d in Department.objects.all():
        print(f"  - {d.name}: ${d.budget:,.2f}")

    # Increase budget of all departments by 10% atomically in SQL database
    Department.objects.update(budget=F('budget') * 1.1)

    print("\nUpdated Budgets (10% Increase via F() Expression):")
    for d in Department.objects.all():
        print(f"  - {d.name}: ${d.budget:,.2f}")


if __name__ == '__main__':
    run_orm_demonstration()
