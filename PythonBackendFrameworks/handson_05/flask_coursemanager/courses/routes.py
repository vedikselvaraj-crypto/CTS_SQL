"""
================================================================================
FLASK-SQLALCHEMY DATABASE ROUTES (courses/routes.py)
================================================================================
Replaces in-memory data with database queries using SQLAlchemy ORM and JOINs.
================================================================================
"""

from typing import Tuple, Any
from flask import Blueprint, request, jsonify, Response
from database import db
from models import Course, Department, Student, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')


def make_response_json(data: Any, status_code: int = 200) -> Tuple[Response, int]:
    """Helper method returning a consistent JSON API response envelope."""
    if status_code in (200, 201):
        envelope = {"status": "success", "data": data}
    else:
        envelope = {"status": "error", "message": data}
    return jsonify(envelope), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    """Queries all courses from database using SQLAlchemy ORM."""
    courses = Course.query.all()
    courses_data = [course.to_dict() for course in courses]
    return make_response_json(courses_data, 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    """Creates a new Course object and commits transaction to database."""
    payload = request.get_json()
    if not payload:
        return make_response_json("Request body must be valid JSON", 400)

    name = payload.get('name')
    code = payload.get('code')
    credits_val = payload.get('credits', 3)
    dept_id = payload.get('department_id')

    if not name or not code or not dept_id:
        return make_response_json("Missing required fields: 'name', 'code', 'department_id'", 400)

    # Verify department exists
    dept = Department.query.get(dept_id)
    if not dept:
        return make_response_json(f"Department with id {dept_id} does not exist", 400)

    # Create and commit new course instance
    new_course = Course(
        name=name,
        code=code,
        credits=int(credits_val),
        department_id=int(dept_id)
    )
    db.session.add(new_course)
    db.session.commit()

    return make_response_json(new_course.to_dict(), 201)


@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course_detail(course_id: int):
    """Retrieves course by ID using get_or_404 ORM shortcut."""
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id: int):
    """Updates course fields and commits transaction."""
    course = Course.query.get_or_404(course_id)
    payload = request.get_json()

    if not payload:
        return make_response_json("Invalid payload", 400)

    course.name = payload.get('name', course.name)
    course.code = payload.get('code', course.code)
    course.credits = payload.get('credits', course.credits)
    if 'department_id' in payload:
        course.department_id = payload['department_id']

    db.session.commit()
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id: int):
    """Deletes course by ID."""
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return make_response_json(f"Course '{course.code}' deleted successfully", 200)


@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id: int):
    """Executes a SQL JOIN query to return all students enrolled in the specified course."""
    course = Course.query.get_or_404(course_id)

    # Perform SQL JOIN query: Student JOIN Enrollment
    enrolled_students = (
        db.session.query(Student)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .filter(Enrollment.course_id == course_id)
        .all()
    )

    students_data = [student.to_dict() for student in enrolled_students]
    return make_response_json({
        "course_id": course.id,
        "course_code": course.code,
        "total_enrolled": len(students_data),
        "students": students_data
    }, 200)
