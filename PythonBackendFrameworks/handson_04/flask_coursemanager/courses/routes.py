"""
================================================================================
FLASK COURSES BLUEPRINT AND ROUTES (courses/routes.py)
================================================================================
"""

from typing import Tuple, Any, Dict
from flask import Blueprint, request, jsonify, Response

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# In-memory storage dictionary for Hands-On 4
in_memory_courses: Dict[int, Dict[str, Any]] = {
    1: {"id": 1, "name": "Intro to Python Programming", "code": "CS-101", "credits": 3},
    2: {"id": 2, "name": "Data Structures & Algorithms", "code": "CS-201", "credits": 4}
}
next_id = 3


def make_response_json(data: Any, status_code: int = 200) -> Tuple[Response, int]:
    """Helper method returning a consistent JSON API response envelope."""
    if status_code in (200, 201):
        envelope = {"status": "success", "data": data}
    else:
        envelope = {"status": "error", "message": data}
    return jsonify(envelope), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    """Returns list of all courses."""
    courses_list = list(in_memory_courses.values())
    return make_response_json(courses_list, 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    """Creates a new course with body payload validation."""
    global next_id
    payload = request.get_json()

    if not payload:
        return make_response_json("Request body must be valid JSON application/json", 400)

    # Validate required fields
    required_fields = ['name', 'code', 'credits']
    missing_fields = [field for field in required_fields if field not in payload or not payload[field]]

    if missing_fields:
        return make_response_json(f"Missing required fields: {', '.join(missing_fields)}", 400)

    new_course = {
        "id": next_id,
        "name": str(payload['name']),
        "code": str(payload['code']),
        "credits": int(payload['credits'])
    }
    in_memory_courses[next_id] = new_course
    next_id += 1

    return make_response_json(new_course, 201)


@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course_detail(course_id: int):
    """Retrieves single course by ID."""
    if course_id not in in_memory_courses:
        return make_response_json(f"Course with id {course_id} not found", 404)
    return make_response_json(in_memory_courses[course_id], 200)


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id: int):
    """Updates course by ID."""
    if course_id not in in_memory_courses:
        return make_response_json(f"Course with id {course_id} not found", 404)

    payload = request.get_json()
    if not payload:
        return make_response_json("Invalid JSON body", 400)

    course = in_memory_courses[course_id]
    course['name'] = payload.get('name', course['name'])
    course['code'] = payload.get('code', course['code'])
    course['credits'] = payload.get('credits', course['credits'])

    return make_response_json(course, 200)


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id: int):
    """Deletes course by ID."""
    if course_id not in in_memory_courses:
        return make_response_json(f"Course with id {course_id} not found", 404)

    deleted_course = in_memory_courses.pop(course_id)
    return make_response_json(f"Course '{deleted_course['name']}' deleted successfully", 200)
