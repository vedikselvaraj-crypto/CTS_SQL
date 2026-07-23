"""
================================================================================
FASTAPI V1 COURSES ROUTER (routers/v1_courses.py)
================================================================================
Follows strict REST conventions: Plural naming, Location headers, PUT vs PATCH,
offset pagination envelopes, and search filters.
================================================================================
"""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_

from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/v1/courses", tags=["V1 Courses"])


"""
================================================================================
ARCHITECTURAL DISCUSSION: API VERSIONING STRATEGY COMPARISON
================================================================================
1. URL Path Versioning (/api/v1/courses/):
   - Pros: Simple, explicit, transparent, highly cacheable by CDN proxies, easy to 
     test in browser address bar.
   - Cons: Pollutes URL space; requires updating client endpoints when major version changes.

2. Header-Based Versioning (Accept: application/vnd.api+json;version=1):
   - Pros: Keeps URLs clean and resource-focused. Follows pure REST principles.
   - Cons: Harder to test manually in browser; CDNs require custom Vary headers to cache.

Decision: URL Path Versioning (/api/v1/) is implemented for maximum clarity.
================================================================================
"""


@router.get("/", response_model=schemas.PaginatedResponse[schemas.CourseResponse], summary="List courses with pagination and search filter")
async def list_courses_v1(
    request: Request,
    page: int = Query(1, ge=1, description="1-based page index"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Case-insensitive search string matching code or name"),
    db: AsyncSession = Depends(get_db)
):
    # Base Query
    query = select(models.Course)
    count_query = select(func.count(models.Course.id))

    # Apply Case-Insensitive Search Filter (ILIKE)
    if search:
        search_filter = or_(
            models.Course.name.ilike(f"%{search}%"),
            models.Course.code.ilike(f"%{search}%")
        )
        query = query.where(search_filter)
        count_query = count_query.where(search_filter)

    # Get total count
    total_result = await db.execute(count_query)
    total_count = total_result.scalar() or 0

    # Apply offset pagination
    offset = (page - 1) * page_size
    query = query.offset(offset).limit(page_size)
    
    result = await db.execute(query)
    courses = result.scalars().all()

    # Construct Next/Previous URLs
    base_url_str = str(request.url).split('?')[0]
    next_url = f"{base_url_str}?page={page + 1}&page_size={page_size}" if (offset + page_size) < total_count else None
    prev_url = f"{base_url_str}?page={page - 1}&page_size={page_size}" if page > 1 else None

    return {
        "count": total_count,
        "next": next_url,
        "previous": prev_url,
        "results": courses
    }


@router.post("/", response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, summary="Create course with Location header")
async def create_course_v1(
    course_data: schemas.CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    new_course = models.Course(**course_data.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    # REST Best Practice: Add Location response header pointing to newly created resource
    response.headers["Location"] = f"/api/v1/courses/{new_course.id}/"
    return new_course


@router.get("/{course_id}/", response_model=schemas.CourseResponse, summary="Get course by ID")
async def get_course_v1(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} does not exist"
        )
    return course


@router.put("/{course_id}/", response_model=schemas.CourseResponse, summary="PUT Full Replace Update")
async def full_update_course_v1(course_id: int, course_data: schemas.CoursePutUpdate, db: AsyncSession = Depends(get_db)):
    """PUT replaces the ENTIRE resource. All fields are required."""
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} does not exist"
        )

    course.name = course_data.name
    course.code = course_data.code
    course.credits = course_data.credits
    course.department_id = course_data.department_id

    await db.commit()
    await db.refresh(course)
    return course


@router.patch("/{course_id}/", response_model=schemas.CourseResponse, summary="PATCH Partial Update")
async def partial_update_course_v1(course_id: int, course_data: schemas.CoursePatchUpdate, db: AsyncSession = Depends(get_db)):
    """PATCH updates ONLY supplied fields. Unsupplied fields remain unchanged."""
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} does not exist"
        )

    for field, value in course_data.model_dump(exclude_unset=True).items():
        setattr(course, field, value)

    await db.commit()
    await db.refresh(course)
    return course


@router.delete("/{course_id}/", status_code=status.HTTP_204_NO_CONTENT, summary="Delete course")
async def delete_course_v1(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).where(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} does not exist"
        )

    await db.delete(course)
    await db.commit()
    return None
