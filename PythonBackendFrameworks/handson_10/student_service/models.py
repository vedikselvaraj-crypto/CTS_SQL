"""
================================================================================
STUDENT SERVICE ORM MODELS (models.py)
================================================================================
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    enrollments = db.relationship('Enrollment', back_populates='student')

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, nullable=False)  # Foreign course_id stored as reference

    student = db.relationship('Student', back_populates='enrollments')

    def to_dict(self):
        return {"id": self.id, "student_id": self.student_id, "course_id": self.course_id}
