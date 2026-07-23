"""
================================================================================
FASTAPI ASYNC ORM MODELS (models.py)
================================================================================
"""

from typing import List, Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    head_of_dept: Mapped[str] = mapped_column(String(100), nullable=False)

    courses: Mapped[List["Course"]] = relationship("Course", back_populates="department", cascade="all, delete-orphan")


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    code: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    credits: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("departments.id"), nullable=False)

    department: Mapped[Department] = relationship("Department", back_populates="courses")
