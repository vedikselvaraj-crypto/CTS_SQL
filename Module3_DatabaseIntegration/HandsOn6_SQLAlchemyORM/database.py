"""
================================================================================
SQLALCHEMY ENGINE & SESSION FACTORY (database.py)
================================================================================
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import DATABASE_URI

# Enable echo=True to print generated SQL statements to terminal (critical for N+1 detection)
engine = create_engine(DATABASE_URI, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    """Base declarative class for all SQLAlchemy ORM models."""
    pass
