"""
================================================================================
FASTAPI ASYNC ORM MODELS (models.py)
================================================================================
"""

from typing import List, Optional
from sqlalchemy import String, Integer, ForeignKey, Date, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    head_of_dept: Mapped[str] = mapped_column(String(100), nullable=False)

    courses: Mapped[List["Course"]] = relationship("Course", back_populates="department", cascade="all, delete-orphan")
    students: Mapped[List["Student"]] = relationship("Student", back_populates="department", cascade="all, delete-orphan")


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    code: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    credits: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("departments.id"), nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="courses")
    enrollments: Mapped[List["Enrollment"]] = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("departments.id"), nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="students")
    enrollments: Mapped[List["Enrollment"]] = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")


class Enrollment(Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("student_id", "course_id", name="unique_student_course"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey("courses.id"), nullable=False)
    grade: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)

    student: Mapped[Student] = relationship("Student", back_populates="enrollments")
    course: Mapped[Course] = relationship("Course", back_populates="enrollments")
