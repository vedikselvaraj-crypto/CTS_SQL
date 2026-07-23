"""
================================================================================
FLASK-SQLALCHEMY ORM MODELS (models.py)
================================================================================
Defines database models, relationships, and to_dict() serialization helpers.
================================================================================
"""

from typing import Dict, Any
from database import db


class Department(db.Model):
    """Department Model."""
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    head_of_dept = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, default=0.0)

    # Relationships
    courses = db.relationship('Course', back_populates='department', cascade='all, delete-orphan')
    students = db.relationship('Student', back_populates='department', cascade='all, delete-orphan')

    def to_dict(self) -> Dict[str, Any]:
        """Serializes Department model instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "head_of_dept": self.head_of_dept,
            "budget": self.budget
        }


class Course(db.Model):
    """Course Model."""
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, default=3, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    # Relationships
    department = db.relationship('Department', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course', cascade='all, delete-orphan')

    def to_dict(self) -> Dict[str, Any]:
        """Serializes Course model instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "department_id": self.department_id,
            "department_name": self.department.name if self.department else None
        }


class Student(db.Model):
    """Student Model."""
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    enrollment_year = db.Column(db.Integer, default=2026, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    # Relationships
    department = db.relationship('Department', back_populates='students')
    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')

    def to_dict(self) -> Dict[str, Any]:
        """Serializes Student model instance to dictionary."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "enrollment_year": self.enrollment_year,
            "department_id": self.department_id,
            "department_name": self.department.name if self.department else None
        }


class Enrollment(db.Model):
    """Enrollment Junction Table Model."""
    __tablename__ = 'enrollments'
    __table_args__ = (db.UniqueConstraint('student_id', 'course_id', name='unique_student_course_enrollment'),)

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrollment_date = db.Column(db.Date, server_default=db.func.current_date())
    grade = db.Column(db.String(5), nullable=True)

    # Relationships
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    def to_dict(self) -> Dict[str, Any]:
        """Serializes Enrollment model instance to dictionary."""
        return {
            "id": self.id,
            "student_id": self.student_id,
            "student_name": f"{self.student.first_name} {self.student.last_name}" if self.student else None,
            "course_id": self.course_id,
            "course_code": self.course.code if self.course else None,
            "enrollment_date": str(self.enrollment_date) if self.enrollment_date else None,
            "grade": self.grade
        }
