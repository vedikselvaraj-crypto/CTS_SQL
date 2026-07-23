"""
================================================================================
FASTAPI STUDENTS ROUTER (routers/students.py)
================================================================================
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("/", response_model=List[schemas.StudentResponse], summary="List all students")
async def list_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Student))
    return result.scalars().all()


@router.post("/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED, summary="Create a student")
async def create_student(student: schemas.StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student


@router.get("/{student_id}", response_model=schemas.StudentResponse, summary="Get student by ID")
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Student).where(models.Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete student")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Student).where(models.Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    await db.delete(student)
    await db.commit()
    return None
