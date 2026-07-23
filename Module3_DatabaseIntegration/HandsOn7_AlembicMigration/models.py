"""
================================================================================
EVOLVING ORM MODELS FOR ALEMBIC MIGRATIONS (models.py)
================================================================================
"""

from typing import List, Optional
from datetime import date
from sqlalchemy import String, Integer, Float, ForeignKey, Date, Boolean, Time, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base declarative class for Alembic target_metadata discovery."""
    pass


class Department(Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dept_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    head_of_dept: Mapped[str] = mapped_column(String(100), nullable=False)
    budget: Mapped[float] = mapped_column(Float, default=0.0)

    courses: Mapped[List["Course"]] = relationship("Course", back_populates="department")
    students: Mapped[List["Student"]] = relationship("Student", back_populates="department")


class Course(Base):
    __tablename__ = 'courses'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    course_name: Mapped[str] = mapped_column(String(150), nullable=False)
    course_code: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    credits: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'), nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="courses")
    schedules: Mapped[List["CourseSchedule"]] = relationship("CourseSchedule", back_populates="course")


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    enrollment_year: Mapped[int] = mapped_column(Integer, default=2026, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'), nullable=False)
    
    # Task 2 Step 98: Added column in Revision 002
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default="1", nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="students")


class Enrollment(Base):
    __tablename__ = 'enrollments'
    __table_args__ = (UniqueConstraint('student_id', 'course_id', name='uq_student_course'),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'), nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'), nullable=False)
    enrollment_date: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)
    grade: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)


class Professor(Base):
    __tablename__ = 'professors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    prof_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'), nullable=False)
    salary: Mapped[float] = mapped_column(Float, default=0.0)


# Task 2 Step 102: Added table in Revision 003
class CourseSchedule(Base):
    __tablename__ = 'course_schedules'

    schedule_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'), nullable=False)
    day_of_week: Mapped[str] = mapped_column(String(15), nullable=False)  # e.g., "Monday", "Wednesday"
    start_time: Mapped[str] = mapped_column(String(10), nullable=False)  # e.g., "09:00 AM"
    end_time: Mapped[str] = mapped_column(String(10), nullable=False)    # e.g., "10:30 AM"

    course: Mapped[Course] = relationship("Course", back_populates="schedules")
