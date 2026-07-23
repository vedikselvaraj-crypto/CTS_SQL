"""
================================================================================
FASTAPI SECURITY & CORS MAIN APPLICATION (main.py)
================================================================================
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import auth_router, courses_router


"""
================================================================================
ARCHITECTURAL & SECURITY ANALYSIS:
--------------------------------------------------------------------------------
1. OAUTH2 AUTHORIZATION CODE FLOW VS. SIMPLE DIRECT JWT LOGIN:
   - Simple Direct JWT Login (Implemented Here):
     The client submits username/password directly to /api/v1/auth/login. The API 
     validates credentials against DB and returns a signed JWT. Best for single-page 
     apps (SPAs) and first-party mobile clients.
   - OAuth2 Authorization Code Flow with PKCE:
     Used when 3rd-party applications need delegated access without touching user 
     credentials. The user is redirected to an Identity Provider (IdP) login page 
     (e.g., Google/Okta), grants consent, receives an Authorization Code via browser 
     redirect, and the client backend exchanges the code for tokens.

2. OWASP TOP 10 SECURITY MITIGATIONS IMPLEMENTED:
   - A01:2021-Broken Access Control: Enforced via Depends(get_current_user) on write routes.
   - A02:2021-Cryptographic Failures: Password hashing via bcrypt work factor & 
     signed JWT payload expiration.
   - A03:2021-Injection: Prevented by SQLAlchemy ORM parametrized SQL queries.
   - A07:2021-Identification & Authentication Failures: Generic 401 error messaging 
     prevents user enumeration.
================================================================================
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Course Management Security & Auth Platform",
    description="JWT Bearer Authentication, Passlib Bcrypt Hashing, and CORS middleware.",
    version="1.0.0",
    lifespan=lifespan
)

# Configure Cross-Origin Resource Sharing (CORS) Middleware
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth_router.router)
app.include_router(courses_router.router)


@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "secure", "auth_mechanism": "JWT Bearer"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
