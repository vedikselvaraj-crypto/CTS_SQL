"""
================================================================================
STUDENT MICROSERVICE APPLICATION (app.py)
================================================================================
Runs on Port 5002 with independent student_service.db database.
Performs synchronous HTTP inter-service verification calls to Course Service (5001).
================================================================================
"""

import os
import requests
from flask import Flask, request, jsonify
from models import db, Student, Enrollment

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'student_service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

COURSE_SERVICE_URL = "http://localhost:5001/api/courses/"


@app.route('/api/students/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify({"service": "Student Service", "data": [s.to_dict() for s in students]}), 200


@app.route('/api/students/', methods=['POST'])
def create_student():
    payload = request.get_json()
    if not payload or 'name' not in payload or 'email' not in payload:
        return jsonify({"error": "Missing required fields: 'name', 'email'"}), 400

    student = Student(name=payload['name'], email=payload['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify({"service": "Student Service", "data": student.to_dict()}), 201


@app.route('/api/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id: int):
    """Enrollment endpoint executing synchronous HTTP inter-service verification."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": f"Student with id {student_id} not found"}), 404

    payload = request.get_json()
    if not payload or 'course_id' not in payload:
        return jsonify({"error": "Missing 'course_id' in payload"}), 400

    course_id = payload['course_id']

    # --------------------------------------------------------------------------
    # SYNCHRONOUS INTER-SERVICE COMMUNICATION VIA REQUESTS HTTP CLIENT
    # --------------------------------------------------------------------------
    print(f"[INTER-SERVICE] Calling Course Service: {COURSE_SERVICE_URL}{course_id}/")
    try:
        response = requests.get(f"{COURSE_SERVICE_URL}{course_id}/", timeout=3.0)
        
        if response.status_code == 404:
            return jsonify({
                "error": f"Course verification failed: Course with id {course_id} does not exist in Course Service"
            }), 404

        if response.status_code != 200:
            return jsonify({
                "error": f"Course Service returned unexpected status code {response.status_code}"
            }), 500

    except requests.exceptions.ConnectionError:
        # Gracefully handle microservice dependency outage
        print("[ERROR] Connection to Course Service (Port 5001) failed!")
        return jsonify({
            "error": "Service Unavailable",
            "message": "Course Service (Port 5001) is currently offline or unreachable."
        }), 503

    # Persist enrollment upon successful inter-service verification
    enrollment = Enrollment(student_id=student.id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()

    return jsonify({
        "service": "Student Service",
        "message": f"Student '{student.name}' successfully enrolled in course id {course_id}",
        "enrollment": enrollment.to_dict()
    }), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Student.query.first():
            db.session.add(Student(id=1, name="Alice Smith", email="alice@college.edu"))
            db.session.commit()

    print("[INFO] Starting Student Microservice on Port 5002...")
    app.run(host='0.0.0.0', port=5002, debug=True)
