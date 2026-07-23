"""
================================================================================
PYDANTIC REQUEST / RESPONSE SCHEMAS (schemas.py)
================================================================================
"""

from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class CourseBase(BaseModel):
    name: str = Field(..., example="Intro to Computer Science", description="Course title")
    code: str = Field(..., example="CS-101", description="Unique course code")
    credits: int = Field(default=3, ge=1, le=10, description="Credit points (1-10)")
    department_id: int = Field(..., description="ID of department offering course")


class CourseCreate(CourseBase):
    """Schema for creating a new Course."""
    pass


class CourseUpdate(BaseModel):
    """Schema for updating a Course; all fields optional."""
    name: Optional[str] = Field(None, example="Advanced Computer Science")
    code: Optional[str] = Field(None, example="CS-102")
    credits: Optional[int] = Field(None, ge=1, le=10)
    department_id: Optional[int] = Field(None)


class CourseResponse(CourseBase):
    """Schema for returning Course data."""
    id: int

    model_config = ConfigDict(from_attributes=True)


class DepartmentBase(BaseModel):
    name: str = Field(..., example="Computer Science")
    head_of_dept: str = Field(..., example="Dr. Alan Turing")


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    """Schema for returning Department details with nested Courses list."""
    id: int
    courses: List[CourseResponse] = []

    model_config = ConfigDict(from_attributes=True)
