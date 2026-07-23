"""
================================================================================
FASTAPI ENROLLMENTS ROUTER WITH BACKGROUND TASKS (routers/enrollments.py)
================================================================================
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/enrollments", tags=["Enrollments"])


def send_confirmation_email(student_email: str):
    """Background task simulating automated email dispatch."""
    print(f"\n[BACKGROUND TASK] Sending enrollment confirmation email to {student_email}...\n")


@router.get("/", response_model=List[schemas.EnrollmentResponse], summary="List all enrollments")
async def list_enrollments(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Enrollment))
    return result.scalars().all()


@router.post("/", response_model=schemas.EnrollmentResponse, status_code=status.HTTP_201_CREATED, summary="Enroll student in course", response_description="Enrolls student and triggers background email confirmation")
async def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    # Verify student exists
    s_res = await db.execute(select(models.Student).where(models.Student.id == enrollment.student_id))
    student = s_res.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    # Verify course exists
    c_res = await db.execute(select(models.Course).where(models.Course.id == enrollment.course_id))
    course = c_res.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    new_enrollment = models.Enrollment(**enrollment.model_dump())
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    # Trigger non-blocking asynchronous background task
    background_tasks.add_task(send_confirmation_email, student.email)

    return new_enrollment
