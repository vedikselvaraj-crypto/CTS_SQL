"""
================================================================================
HANDS-ON 6 - TASK 2: FULL ORM CRUD OPERATIONS SCRIPT (crud.py)
================================================================================
Executes table creation, session management, INSERT, READ (JOINs), UPDATE, and DELETE.
================================================================================
"""

from datetime import date
from database import engine, Base, SessionLocal
from models import Department, Student, Course, Enrollment, Professor


def run_crud_operations():
    print("\n[INFO] Step 79: Auto-creating database tables via Base.metadata.create_all(engine)...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = SessionLocal()

    try:
        print("\n=== STEP 81: INSERT 3 Departments and 5 Students ===")
        cs_dept = Department(dept_name="Computer Science", head_of_dept="Dr. Alan Turing", budget=850000.0)
        ee_dept = Department(dept_name="Electronics", head_of_dept="Dr. Nikola Tesla", budget=620000.0)
        me_dept = Department(dept_name="Mechanical", head_of_dept="Dr. Suresh Iyer", budget=540000.0)
        session.add_all([cs_dept, ee_dept, me_dept])
        session.commit()

        s1 = Student(first_name="Arjun", last_name="Mehta", email="arjun@college.edu", date_of_birth=date(2003, 4, 12), department_id=cs_dept.id, enrollment_year=2022)
        s2 = Student(first_name="Priya", last_name="Suresh", email="priya@college.edu", date_of_birth=date(2003, 7, 25), department_id=cs_dept.id, enrollment_year=2022)
        s3 = Student(first_name="Rohan", last_name="Verma", email="rohan@college.edu", date_of_birth=date(2002, 11, 8), department_id=ee_dept.id, enrollment_year=2021)
        s4 = Student(first_name="Sneha", last_name="Patel", email="sneha@college.edu", date_of_birth=date(2004, 1, 30), department_id=me_dept.id, enrollment_year=2023)
        s5 = Student(first_name="Vikram", last_name="Das", email="vikram@college.edu", date_of_birth=date(2003, 9, 14), department_id=cs_dept.id, enrollment_year=2022)
        session.add_all([s1, s2, s3, s4, s5])
        session.commit()
        print("[SUCCESS] Inserted 3 Departments and 5 Students.")

        print("\n=== STEP 82: INSERT 3 Courses and 4 Enrollments ===")
        c1 = Course(course_name="Data Structures", course_code="CS101", credits=4, department_id=cs_dept.id)
        c2 = Course(course_name="Database Systems", course_code="CS102", credits=3, department_id=cs_dept.id)
        c3 = Course(course_name="Circuit Theory", course_code="EC101", credits=3, department_id=ee_dept.id)
        session.add_all([c1, c2, c3])
        session.commit()

        e1 = Enrollment(student_id=s1.id, course_id=c1.id, grade="A")
        e2 = Enrollment(student_id=s1.id, course_id=c2.id, grade="B")
        e3 = Enrollment(student_id=s2.id, course_id=c1.id, grade="A")
        e4 = Enrollment(student_id=s3.id, course_id=c3.id, grade="B+")
        session.add_all([e1, e2, e3, e4])
        session.commit()
        print("[SUCCESS] Inserted 3 Courses and 4 Enrollments.")

        print("\n=== STEP 83: READ - Query Students in 'Computer Science' via JOIN ===")
        cs_students = session.query(Student).join(Department).filter(Department.dept_name == "Computer Science").all()
        print(f"Found {len(cs_students)} CS Students:")
        for st in cs_students:
            print(f"  - Student: {st.first_name} {st.last_name} ({st.email})")

        print("\n=== STEP 84: READ - Query Enrollments & Print Student Name with Course Name ===")
        enrollments = session.query(Enrollment).all()
        for enr in enrollments:
            print(f"  - Student '{enr.student.first_name} {enr.student.last_name}' -> Course '{enr.course.course_name}' (Grade: {enr.grade})")

        print("\n=== STEP 85: UPDATE - Update Student Enrollment Year by Email ===")
        student_to_update = session.query(Student).filter(Student.email == "arjun@college.edu").first()
        if student_to_update:
            print(f"Original Enrollment Year for {student_to_update.email}: {student_to_update.enrollment_year}")
            student_to_update.enrollment_year = 2025
            session.commit()
            print(f"Updated Enrollment Year: {student_to_update.enrollment_year}")

        print("\n=== STEP 86: DELETE - Remove an Enrollment Record ===")
        enrollment_to_delete = session.query(Enrollment).filter(Enrollment.id == e4.id).first()
        if enrollment_to_delete:
            print(f"Deleting Enrollment Record ID: {enrollment_to_delete.id}")
            session.delete(enrollment_to_delete)
            session.commit()

        remaining_count = session.query(Enrollment).count()
        print(f"[VERIFICATION] Remaining Enrollments Count: {remaining_count}")

    except Exception as e:
        session.rollback()
        print(f"[ERROR] Transaction rolled back due to error: {e}")
        raise e
    finally:
        session.close()


if __name__ == "__main__":
    run_crud_operations()
