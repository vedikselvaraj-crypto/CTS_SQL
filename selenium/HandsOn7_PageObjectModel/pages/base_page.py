"""
================================================================================
HANDS-ON 7: BASE PAGE CLASS (base_page.py)
================================================================================
Superclass for all Page Objects. Encapsulates WebDriver instance and provides 
common UI interaction wrappers, dynamic waits, and error handling.
================================================================================
"""

from typing import Tuple, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class providing common element interactions and navigation for all page objects."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.default_timeout = 10

    def navigate_to(self, url: str) -> None:
        """Navigates browser to target URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Returns current page title string."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Returns current browser URL string."""
        return self.driver.current_url

    def wait_for_element(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """Explicitly waits for element to be visible in DOM."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element locator {locator} was not visible after {timeout} seconds."
        )

    def wait_for_clickable(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """Explicitly waits for element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Element locator {locator} was not clickable after {timeout} seconds."
        )

    def find(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """Finds and returns a single element after waiting for visibility."""
        return self.wait_for_element(locator, timeout)

    def find_all(self, locator: Tuple[str, str], timeout: int = 10) -> List[WebElement]:
        """Waits for presence of all elements matching locator and returns list."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"No elements matching {locator} were found after {timeout} seconds."
        )

    def click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        """Waits for element to be clickable and executes click."""
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def type_text(self, locator: Tuple[str, str], text: str, timeout: int = 10) -> None:
        """Waits for element, clears existing content, and sends keys."""
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str], timeout: int = 10) -> str:
        """Waits for element and returns inner text string."""
        element = self.wait_for_element(locator, timeout)
        return element.text

    def is_selected(self, locator: Tuple[str, str], timeout: int = 10) -> bool:
        """Returns selection state of checkbox or radio button."""
        element = self.wait_for_element(locator, timeout)
        return element.is_selected()
