"""
================================================================================
SQLALCHEMY 2.0 ORM MODELS (models.py)
================================================================================
Defines 5 core database entities and bidirectional relationship properties.
================================================================================
"""

from typing import List, Optional
from datetime import date
from sqlalchemy import String, Integer, Float, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Department(Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dept_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    head_of_dept: Mapped[str] = mapped_column(String(100), nullable=False)
    budget: Mapped[float] = mapped_column(Float, default=0.0)

    courses: Mapped[List["Course"]] = relationship("Course", back_populates="department", cascade="all, delete-orphan")
    students: Mapped[List["Student"]] = relationship("Student", back_populates="department", cascade="all, delete-orphan")
    professors: Mapped[List["Professor"]] = relationship("Professor", back_populates="department", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Department(id={self.id}, dept_name='{self.dept_name}')>"


class Course(Base):
    __tablename__ = 'courses'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    course_name: Mapped[str] = mapped_column(String(150), nullable=False)
    course_code: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    credits: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'), nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="courses")
    enrollments: Mapped[List["Enrollment"]] = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Course(code='{self.course_code}', name='{self.course_name}')>"


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    enrollment_year: Mapped[int] = mapped_column(Integer, default=2026, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'), nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="students")
    enrollments: Mapped[List["Enrollment"]] = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}')>"


class Enrollment(Base):
    __tablename__ = 'enrollments'
    __table_args__ = (UniqueConstraint('student_id', 'course_id', name='uq_student_course_enrollment'),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'), nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'), nullable=False)
    enrollment_date: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)
    grade: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)

    student: Mapped[Student] = relationship("Student", back_populates="enrollments")
    course: Mapped[Course] = relationship("Course", back_populates="enrollments")

    def __repr__(self) -> str:
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, grade='{self.grade}')>"


class Professor(Base):
    __tablename__ = 'professors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    prof_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'), nullable=False)
    salary: Mapped[float] = mapped_column(Float, default=0.0)

    department: Mapped[Department] = relationship("Department", back_populates="professors")

    def __repr__(self) -> str:
        return f"<Professor(name='{self.prof_name}', salary={self.salary})>"
