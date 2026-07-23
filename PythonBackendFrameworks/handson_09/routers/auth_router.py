"""
================================================================================
AUTHENTICATION ROUTER (routers/auth_router.py)
================================================================================
Handles user registration, bcrypt password hashing, and JWT login authentication.
================================================================================
"""

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
import models
import schemas
from security import get_password_hash, verify_password
from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@router.post("/register/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED, summary="Register a new user")
async def register_user(user_data: schemas.UserRegister, db: AsyncSession = Depends(get_db)):
    """Validates email, verifies uniqueness (returns 409 if duplicate), hashes 
    password via bcrypt, and persists user.
    """
    # Check duplicate email
    result = await db.execute(select(models.User).where(models.User.email == user_data.email))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Email '{user_data.email}' is already registered."
        )

    # Hash plain-text password using bcrypt work factor
    hashed_pwd = get_password_hash(user_data.password)

    new_user = models.User(
        email=user_data.email,
        hashed_password=hashed_pwd,
        is_active=True
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@router.post("/login/", response_model=schemas.Token, summary="Login to obtain JWT Bearer Token")
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """Authenticates user credentials and returns JWT Bearer access token."""
    result = await db.execute(select(models.User).where(models.User.email == form_data.username))
    user = result.scalar_one_or_none()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
