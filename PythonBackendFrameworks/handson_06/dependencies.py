"""
================================================================================
FASTAPI DEPENDENCIES (dependencies.py)
================================================================================
Re-exports database dependencies and custom application dependencies.
================================================================================
"""

from database import get_db

__all__ = ["get_db"]
