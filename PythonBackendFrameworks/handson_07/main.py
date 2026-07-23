"""
================================================================================
FASTAPI MAIN ENTRY POINT WITH CUSTOM OPENAPI METADATA (main.py)
================================================================================
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from routers import courses, students, enrollments


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Course Management Enterprise API",
    description=(
        "Production-grade FastAPI implementation for managing university departments, "
        "courses, student registrations, and enrollments with async database sessions "
        "and non-blocking background workers."
    ),
    version="2.0.0",
    contact={
        "name": "Principal Backend Architect",
        "email": "architect@college.edu",
        "url": "https://college.edu/api/docs"
    },
    lifespan=lifespan
)

# Register Router Modules
app.include_router(courses.router)
app.include_router(students.router)
app.include_router(enrollments.router)


@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "healthy", "service": "Course Management API v2.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
