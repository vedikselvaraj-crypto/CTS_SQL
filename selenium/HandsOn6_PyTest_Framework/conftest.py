"""
================================================================================
HANDS-ON 6: SHARED PYTEST FIXTURES & SCREENSHOT HOOK (conftest.py)
================================================================================
Defines function-scoped driver fixtures, session-scoped base_url fixtures,
and automated screenshot capture on test failure using pytest hooks.
================================================================================
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url() -> str:
    """Session-scoped fixture providing target application base URL constant."""
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver(request):
    """Function-scoped fixture initializing a fresh Chrome WebDriver instance per test
    and cleanly quitting browser after yield.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    browser_instance = webdriver.Chrome(service=service, options=options)
    browser_instance.implicitly_wait(5)

    # Attach driver reference to request node for pytest failure hook access
    request.node.driver = browser_instance

    yield browser_instance

    # Teardown phase after test completion
    browser_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """PyTest hook capturing screenshot automatically on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Retrieve driver instance from item node or funcargs
        driver_instance = getattr(item, "driver", None) or item.funcargs.get("driver")
        if driver_instance:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            screenshots_dir = os.path.join(current_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            test_name = item.name.replace("[", "_").replace("]", "_").replace("-", "_")
            screenshot_path = os.path.join(screenshots_dir, f"{test_name}_failure.png")
            
            driver_instance.save_screenshot(screenshot_path)
            print(f"\n[HOOK] Screenshot captured on test failure: {screenshot_path}")
