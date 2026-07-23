"""
================================================================================
HANDS-ON 7: REUSABLE WAIT UTILITIES (wait_utils.py)
================================================================================
Encapsulates custom explicit wait conditions and helper utilities.
================================================================================
"""

from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    """Helper class encapsulating explicit wait conditions."""

    def __init__(self, driver: WebDriver, default_timeout: int = 10) -> None:
        self.driver = driver
        self.default_timeout = default_timeout

    def wait_for_visibility(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        """Waits for element to be visible in DOM."""
        t = timeout or self.default_timeout
        return WebDriverWait(self.driver, t).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} not visible after {t} seconds."
        )

    def wait_for_clickable(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        """Waits for element to be visible, enabled, and clickable."""
        t = timeout or self.default_timeout
        return WebDriverWait(self.driver, t).until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} not clickable after {t} seconds."
        )

    def wait_for_text(self, locator: Tuple[str, str], text: str, timeout: int = None) -> bool:
        """Waits for element text to equal or contain specified string."""
        t = timeout or self.default_timeout
        return WebDriverWait(self.driver, t).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Text '{text}' not present in {locator} after {t} seconds."
        )
