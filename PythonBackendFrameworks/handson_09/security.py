"""
================================================================================
PASSLIB BCRYPT SECURITY UTILITIES (security.py)
================================================================================
"""

from passlib.context import CryptContext

# Configure Passlib CryptContext using bcrypt hashing scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


"""
================================================================================
WHY BCRYPT IS PREFERRED OVER MD5 AND SHA-256:
--------------------------------------------------------------------------------
1. Computationally Expensive by Design (Work-Factor / Key-Stretching):
   - Fast hashing algorithms (MD5, SHA-1, SHA-256) were engineered for speed.
     Modern GPUs can compute billions of SHA-256 hashes per second, making rainbow 
     table and dictionary brute-force attacks trivial.
   - Bcrypt incorporates a configurable cost factor (work factor) that intentionally 
     slows down hashing (e.g. 100ms per attempt).

2. Built-In Cryptographic Salt:
   - Bcrypt automatically embeds a unique 128-bit random salt into every generated 
     hash string (e.g. $2b$12$eImiTXuWVxfM37uY4JANjO...). This prevents pre-computed 
     Rainbow Table attacks and guarantees that identical passwords produce completely 
     different stored hashes.
================================================================================
"""


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies plain text password against stored bcrypt hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Generates salted bcrypt hash from plain text password."""
    return pwd_context.hash(password)
