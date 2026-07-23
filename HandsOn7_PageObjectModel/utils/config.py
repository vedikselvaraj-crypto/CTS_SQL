"""
================================================================================
HANDS-ON 7: GLOBAL CONFIGURATION CONSTANTS (config.py)
================================================================================
Centralizes base URLs, timeout thresholds, browser flags, and environment configs.
================================================================================
"""

class Config:
    """Global configuration settings for Page Object Model test suite."""
    BASE_URL: str = "https://www.lambdatest.com/selenium-playground/"
    IMPLICIT_WAIT: int = 0  # Enforce explicit waits across framework
    EXPLICIT_WAIT: int = 10
    HEADLESS: bool = True
    BROWSER: str = "chrome"
