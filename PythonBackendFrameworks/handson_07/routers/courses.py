"""
================================================================================
FASTAPI COURSES ROUTER (routers/courses.py)
================================================================================
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/courses", tags=["Courses"])


@router.get("/", response_model=List[schemas.CourseResponse], summary="List all courses")
async def list_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course))
    return result.scalars().all()


@router.post("/", response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, summary="Create a course")
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = models.Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@router.get("/{course_id}", response_model=schemas.CourseResponse, summary="Get course by ID")
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course


@router.put("/{course_id}", response_model=schemas.CourseResponse, summary="Update course")
async def update_course(course_id: int, course_data: schemas.CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)
    return course


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete course")
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    await db.delete(course)
    await db.commit()
    return None


@router.get("/{course_id}/students", response_model=List[schemas.StudentResponse], summary="List students enrolled in course")
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    """Executes a SQL JOIN query to return all students enrolled in specified course."""
    query = (
        select(models.Student)
        .join(models.Enrollment, models.Student.id == models.Enrollment.student_id)
        .where(models.Enrollment.course_id == course_id)
    )
    result = await db.execute(query)
    students = result.scalars().all()
    return students
