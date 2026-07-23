"""
================================================================================
COURSE MICROSERVICE APPLICATION (app.py)
================================================================================
Runs on Port 5001 with independent course_service.db database.
================================================================================
"""

import os
from flask import Flask, request, jsonify
from models import db, Course

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'course_service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/api/courses/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify({"service": "Course Service", "data": [c.to_dict() for c in courses]}), 200


@app.route('/api/courses/', methods=['POST'])
def create_course():
    payload = request.get_json()
    if not payload or 'name' not in payload or 'code' not in payload:
        return jsonify({"error": "Missing required fields: 'name', 'code'"}), 400

    course = Course(name=payload['name'], code=payload['code'], credits=payload.get('credits', 3))
    db.session.add(course)
    db.session.commit()
    return jsonify({"service": "Course Service", "data": course.to_dict()}), 201


@app.route('/api/courses/<int:course_id>/', methods=['GET'])
def get_course_by_id(course_id: int):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": f"Course with id {course_id} not found"}), 404
    return jsonify({"service": "Course Service", "data": course.to_dict()}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Seed default course if DB is empty
        if not Course.query.first():
            db.session.add(Course(id=1, name="Microservices Architecture", code="CS-901", credits=4))
            db.session.commit()

    print("[INFO] Starting Course Microservice on Port 5001...")
    app.run(host='0.0.0.0', port=5001, debug=True)
