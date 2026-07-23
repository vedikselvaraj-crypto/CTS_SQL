"""
================================================================================
HANDS-ON 5 - TASK 3: FLUENT WAIT IMPLEMENTATION IN SELENIUM PYTHON
================================================================================
Demonstrates Fluent Wait configuration in Python using WebDriverWait with 
custom polling frequencies (e.g., poll every 500ms), maximum timeout, and 
ignoring specific transient exceptions (NoSuchElementException, StaleElementReferenceException).

TARGET: https://www.lambdatest.com/selenium-playground/table-data-download-demo
================================================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException
)
from webdriver_manager.chrome import ChromeDriverManager


def run_fluent_wait_demo() -> None:
    """Configures and executes a Fluent Wait targeting dynamic table row elements."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        table_demo_url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
        print(f"[INFO] Navigating to Table Demo: {table_demo_url}")
        driver.get(table_demo_url)

        # ----------------------------------------------------------------------
        # FLUENT WAIT CONFIGURATION IN SELENIUM PYTHON:
        # ----------------------------------------------------------------------
        # In Python Selenium, Fluent Wait is instantiated via WebDriverWait by passing:
        # 1. timeout=10 (Maximum wait duration in seconds)
        # 2. poll_frequency=0.5 (Poll the DOM every 500 milliseconds)
        # 3. ignored_exceptions=[...] (Exceptions to ignore during polling phase)
        # ----------------------------------------------------------------------
        ignored_exceptions_list = (
            NoSuchElementException,
            ElementNotInteractableException,
            StaleElementReferenceException,
        )

        print("[INFO] Initializing Fluent Wait (Timeout: 10s, Poll Frequency: 500ms)...")
        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=ignored_exceptions_list
        )

        # Perform search interaction that dynamically updates table rows
        search_box_locator = (By.CSS_SELECTOR, "#example_filter input")
        print("[INFO] Typing search query 'Chief Executive Officer' into table filter...")
        
        search_input = fluent_wait.until(EC.visibility_of_element_located(search_box_locator))
        search_input.clear()
        search_input.send_keys("Chief Executive Officer")

        # Apply Fluent Wait to locate dynamically filtered table row
        print("[INFO] Applying Fluent Wait to poll for filtered table row...")
        table_row_locator = (By.XPATH, "//table[@id='example']/tbody/tr[1]")
        
        # Fluent Wait polls DOM every 500ms, suppressing ignored exceptions until element matches condition
        matched_row = fluent_wait.until(
            EC.visibility_of_element_located(table_row_locator),
            message="Timed out waiting for dynamically filtered table row under Fluent Wait!"
        )

        row_text = matched_row.text
        print(f"[SUCCESS] Dynamic Table Row Found via Fluent Wait:\n   '{row_text}'")
        assert "Chief Executive Officer" in row_text, "Filtered row text did not match expected search string!"

    finally:
        print("[INFO] Closing browser session...")
        driver.quit()


if __name__ == "__main__":
    run_fluent_wait_demo()
