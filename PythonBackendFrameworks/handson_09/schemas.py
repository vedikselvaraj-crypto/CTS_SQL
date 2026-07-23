"""
================================================================================
PYDANTIC SCHEMAS FOR AUTH & SECURITY (schemas.py)
================================================================================
"""

from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserRegister(BaseModel):
    email: EmailStr = Field(..., example="user@college.edu")
    password: str = Field(..., min_length=8, example="SecurePassword123!")


class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="user@college.edu")
    password: str = Field(..., example="SecurePassword123!")


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Optional[str] = None


class CourseCreate(BaseModel):
    name: str = Field(..., example="Applied Cryptography")
    code: str = Field(..., example="CS-505")
    credits: int = Field(default=3, ge=1, le=10)


class CourseResponse(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
