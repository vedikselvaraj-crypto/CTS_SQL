"""
================================================================================
HANDS-ON 4 - TASK 1: SELENIUM ARCHITECTURE AND ENVIRONMENT SETUP
================================================================================

SELENIUM ARCHITECTURE OVERVIEW:
--------------------------------------------------------------------------------
1. Selenium WebDriver:
   - What it is: A client library and browser automation API that directly controls 
     browsers natively.
   - Communication Protocol: Uses the W3C WebDriver Standard HTTP protocol to send 
     JSON wire commands to browser-specific drivers (e.g., ChromeDriver for Chrome, 
     GeckoDriver for Firefox). The browser driver translates these commands into native 
     browser engine actions (Blink/V8 for Chrome) and returns HTTP responses back to Python.

2. Selenium Grid:
   - Problem Solved: Enables distributed, parallel test execution across multiple remote 
     nodes, operating systems (Windows, Linux, macOS), and browser combinations.
   - Architecture: Operates on a Hub-Node architecture. The central Hub routes test execution 
     requests to registered Node instances based on capability matching (e.g., browser=Firefox, os=Linux).

3. Selenium IDE:
   - Purpose: A lightweight Chrome/Firefox browser extension used for rapid test prototyping, 
     record-and-playback, and exporting initial script drafts into programming languages 
     (Python, Java, C#). It is non-programmable and not suitable for enterprise test suites.
================================================================================
"""

import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def run_setup_test() -> None:
    """Initializes Chrome WebDriver using webdriver-manager in headless mode,
    configures implicit waits with documentation, navigates to target URL,
    asserts title, and cleans up resources.
    """
    print("[INFO] Setting up Chrome Options...")
    options = Options()
    
    # Enable Headless Mode (runs browser without visible GUI window)
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    print("[INFO] Initializing ChromeDriver via webdriver-manager...")
    # webdriver-manager automatically checks installed Chrome version, downloads 
    # matching ChromeDriver binary, and sets executable path in Service.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # ----------------------------------------------------------------------
        # IMPLICIT WAIT EXPLANATION & WHY IT IS CONSIDERED BAD PRACTICE:
        # ----------------------------------------------------------------------
        # Setting driver.implicitly_wait(10) instructs WebDriver to poll the DOM 
        # for up to 10 seconds whenever ANY find_element call fails.
        #
        # WHY GLOBAL IMPLICIT WAITS ARE BAD PRACTICE:
        # 1. Performance Degradation: Throws unnecessary delays when asserting 
        #    element ABSENCE (e.g., verifying an element is deleted forces 10s wait).
        # 2. Conflict with Explicit Waits: Mixing implicit and explicit waits causes 
        #    unpredictable wait times (e.g., 10s implicit + 10s explicit can result 
        #    in a 20s timeout due to browser driver implementation differences).
        # 3. Lack of Condition Flexibility: Cannot wait for specific states like 
        #    'element to be clickable', 'text to be present', or 'stale element refresh'.
        # ----------------------------------------------------------------------
        driver.implicitly_wait(10)

        target_url = "https://www.lambdatest.com/selenium-playground/"
        print(f"[INFO] Navigating to: {target_url}")
        driver.get(target_url)

        # Retrieve and print page title
        page_title = driver.title
        print(f"[SUCCESS] Page Title: '{page_title}'")

        # Assertion
        assert "Selenium Grid Online" in page_title or "LambdaTest" in page_title, \
            f"Assertion Failed! Title '{page_title}' did not match expected string."
        
        print("[SUCCESS] Page title assertion passed cleanly in headless mode!")

    except Exception as e:
        print(f"[ERROR] Test failed with exception: {e}", file=sys.stderr)
        raise e

    finally:
        print("[INFO] Closing browser session...")
        driver.quit()


if __name__ == "__main__":
    run_setup_test()
