"""
================================================================================
PYDANTIC SCHEMAS WITH STANDARDIZED RESPONSE ENVELOPES (schemas.py)
================================================================================
"""

from typing import Optional, List, Any, Generic, TypeVar
from pydantic import BaseModel, Field, ConfigDict

T = TypeVar('T')


# ------------------------------------------------------------------------------
# STANDARDIZED ERROR RESPONSE ENVELOPE
# ------------------------------------------------------------------------------
class ErrorDetail(BaseModel):
    code: str = Field(..., example="NOT_FOUND", description="Machine-readable error code")
    message: str = Field(..., example="Course with id 99 does not exist", description="Human-readable message")
    field: Optional[str] = Field(None, example="email", description="Validation field name if applicable")


class ErrorResponseEnvelope(BaseModel):
    error: ErrorDetail


# ------------------------------------------------------------------------------
# OFFSET PAGINATION RESPONSE ENVELOPE (DRF Standard)
# ------------------------------------------------------------------------------
class PaginatedResponse(BaseModel, Generic[T]):
    count: int = Field(..., example=42, description="Total matching items in database")
    next: Optional[str] = Field(None, example="http://api.com/v1/courses/?page=2&page_size=10")
    previous: Optional[str] = Field(None, example=None)
    results: List[T]


# ------------------------------------------------------------------------------
# COURSE DOMAIN SCHEMAS
# ------------------------------------------------------------------------------
class CourseBase(BaseModel):
    name: str = Field(..., example="Software Architecture Principles")
    code: str = Field(..., example="CS-501")
    credits: int = Field(default=3, ge=1, le=10)
    department_id: int = Field(..., example=1)


class CourseCreate(CourseBase):
    pass


class CoursePutUpdate(CourseBase):
    """PUT replaces the ENTIRE resource (all fields mandatory)."""
    pass


class CoursePatchUpdate(BaseModel):
    """PATCH updates ONLY supplied fields (all fields optional)."""
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = Field(None, ge=1, le=10)
    department_id: Optional[int] = None


class CourseResponse(CourseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
