"""
================================================================================
PROTECTED COURSES ROUTER (routers/courses_router.py)
================================================================================
Demonstrates endpoint protection using OAuth2 Depends(get_current_user).
================================================================================
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
import models
import schemas
from auth import get_current_user

router = APIRouter(prefix="/api/v1/courses", tags=["Protected Courses"])


@router.get("/", response_model=List[schemas.CourseResponse], summary="List all courses (Public Endpoint)")
async def list_courses(db: AsyncSession = Depends(get_db)):
    """Public endpoint: Anyone can view courses without authentication."""
    result = await db.execute(select(models.Course))
    return result.scalars().all()


@router.post("/", response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, summary="Create a course (Protected: Requires Valid JWT)")
async def create_course(
    course_data: schemas.CourseCreate,
    current_user: models.User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Protected endpoint: Requires valid JWT Bearer token in Authorization header."""
    new_course = models.Course(**course_data.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@router.delete("/{course_id}/", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a course (Protected: Requires Valid JWT)")
async def delete_course(
    course_id: int,
    current_user: models.User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Protected endpoint: Requires valid JWT Bearer token in Authorization header."""
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    await db.delete(course)
    await db.commit()
    return None
