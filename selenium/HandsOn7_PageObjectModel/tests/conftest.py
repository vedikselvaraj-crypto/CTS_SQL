"""
================================================================================
HANDS-ON 7: PYTEST FIXTURES & HOOKS FOR POM SUITE (conftest.py)
================================================================================
Defines browser initialization fixtures using Config settings and automatic 
screenshot capture hooks on test failure.
================================================================================
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from HandsOn7_PageObjectModel.utils.config import Config


@pytest.fixture(scope="session")
def base_url() -> str:
    """Session fixture providing base URL from Config."""
    return Config.BASE_URL


@pytest.fixture(scope="function")
def driver(request):
    """Function fixture providing isolated Chrome driver per test."""
    options = Options()
    if Config.HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
    if Config.IMPLICIT_WAIT > 0:
        browser.implicitly_wait(Config.IMPLICIT_WAIT)

    request.node.driver = browser
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """PyTest hook capturing screenshot automatically on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = getattr(item, "driver", None) or item.funcargs.get("driver")
        if driver_instance:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            screenshots_dir = os.path.join(current_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            test_name = item.name.replace("[", "_").replace("]", "_").replace("-", "_")
            screenshot_path = os.path.join(screenshots_dir, f"{test_name}_failure.png")
            driver_instance.save_screenshot(screenshot_path)
            print(f"\n[POM HOOK] Screenshot captured on test failure: {screenshot_path}")
