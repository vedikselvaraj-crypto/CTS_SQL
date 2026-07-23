"""
================================================================================
FASTAPI MAIN ENTRY POINT (main.py)
================================================================================
Configures FastAPI application, startup database creation, async routes,
Pydantic validations, path/query parameters, and async ORM queries.
================================================================================
"""

from typing import List, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import engine, Base, get_db
import models
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    DepartmentCreate,
    DepartmentResponse
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager creating database tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Course Management API",
    description="FastAPI High-Performance Async Backend Implementation",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", tags=["Health Check"])
async def root():
    """Root health check endpoint."""
    return {"message": "API running"}


@app.post("/api/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED, tags=["Courses"])
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    """Creates a new course with Pydantic body validation."""
    # Check if department exists
    result = await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    dept = result.scalar_one_or_none()
    if not dept:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Department with id {course.department_id} does not exist"
        )

    # Check for duplicate course code
    result_code = await db.execute(select(models.Course).where(models.Course.code == course.code))
    if result_code.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Course code '{course.code}' already exists"
        )

    new_course = models.Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@app.get("/api/courses/{course_id}", response_model=CourseResponse, tags=["Courses"])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieves a single course by integer path parameter course_id."""
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found"
        )
    return course


@app.get("/api/courses/", response_model=List[CourseResponse], tags=["Courses"])
async def get_courses(
    skip: int = Query(0, ge=0, description="Offset for pagination"),
    limit: int = Query(10, ge=1, le=100, description="Page limit size"),
    department_id: Optional[int] = Query(None, description="Optional department filter"),
    db: AsyncSession = Depends(get_db)
):
    """Retrieves a list of courses with optional pagination and department filtering."""
    query = select(models.Course)
    if department_id is not None:
        query = query.where(models.Course.department_id == department_id)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    courses = result.scalars().all()
    return courses


@app.post("/api/departments/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED, tags=["Departments"])
async def create_department(dept: DepartmentCreate, db: AsyncSession = Depends(get_db)):
    """Creates a new department."""
    new_dept = models.Department(**dept.model_dump())
    db.add(new_dept)
    await db.commit()
    await db.refresh(new_dept)
    return new_dept
