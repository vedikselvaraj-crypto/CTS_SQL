"""
================================================================================
PYDANTIC SCHEMAS FOR HANDS-ON 7 (schemas.py)
================================================================================
"""

from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, ConfigDict


# Course Schemas
class CourseBase(BaseModel):
    name: str = Field(..., example="Software Architecture")
    code: str = Field(..., example="CS-401")
    credits: int = Field(default=3, ge=1, le=10)
    department_id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = Field(None, ge=1, le=10)
    department_id: Optional[int] = None


class CourseResponse(CourseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# Student Schemas
class StudentBase(BaseModel):
    first_name: str = Field(..., example="Alice")
    last_name: str = Field(..., example="Smith")
    email: EmailStr = Field(..., example="alice@college.edu")
    department_id: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    department_id: Optional[int] = None


class StudentResponse(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# Enrollment Schemas
class EnrollmentCreate(BaseModel):
    student_id: int = Field(..., example=1)
    course_id: int = Field(..., example=1)
    grade: Optional[str] = Field(None, example="A")


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    grade: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
