"""
================================================================================
FASTAPI MAIN ENTRY POINT WITH STANDARDIZED ERROR ENVELOPES (main.py)
================================================================================
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from database import engine, Base
from routers import v1_courses
import schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="RESTful API Design Standards Platform",
    description="Implements standardized error envelopes, versioning, and DRF offset pagination.",
    version="1.0.0",
    lifespan=lifespan
)


# ------------------------------------------------------------------------------
# STANDARDIZED EXCEPTION HANDLERS
# ------------------------------------------------------------------------------
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """Custom exception handler standardizing all HTTP errors into unified schema format."""
    code_str = "NOT_FOUND" if exc.status_code == 404 else ("CONFLICT" if exc.status_code == 409 else "BAD_REQUEST")
    error_payload = {
        "error": {
            "code": code_str,
            "message": str(exc.detail),
            "field": None
        }
    }
    return JSONResponse(status_code=exc.status_code, content=error_payload)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Custom exception handler standardizing Pydantic validation errors."""
    first_error = exc.errors()[0]
    field_name = ".".join(str(x) for x in first_error.get("loc", []))
    error_payload = {
        "error": {
            "code": "VALIDATION_ERROR",
            "message": first_error.get("msg", "Invalid request body or parameters"),
            "field": field_name
        }
    }
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error_payload)


# Include V1 Router
app.include_router(v1_courses.router)


@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "healthy", "api_version": "v1"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
