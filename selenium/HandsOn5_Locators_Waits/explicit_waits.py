"""
================================================================================
HANDS-ON 5 - TASK 2: WEBDRIVERWAIT AND EXPECTED CONDITIONS
================================================================================
Demonstrates explicit waits using WebDriverWait and ExpectedConditions (EC).
Includes performance timing benchmark comparing time.sleep() vs explicit waits,
and explains element_to_be_clickable vs visibility_of_element_located.

TARGET: https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo
================================================================================
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def run_explicit_waits_demo() -> None:
    """Executes Bootstrap Alert interaction with explicit waits and benchmark tests."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        alert_demo_url = "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"
        print(f"[INFO] Navigating to: {alert_demo_url}")
        driver.get(alert_demo_url)

        # ----------------------------------------------------------------------
        # 1. Clickable Wait Demonstration & Click Action
        # ----------------------------------------------------------------------
        print("[INFO] Waiting for 'Normal Success Message' button to be clickable...")
        # EC.element_to_be_clickable verifies element is present, visible, enabled, and clickable.
        success_btn_locator = (By.XPATH, "//button[contains(text(),'Normal Success Message')]")
        
        wait = WebDriverWait(driver, timeout=10)
        success_btn = wait.until(EC.element_to_be_clickable(success_btn_locator))
        print("[SUCCESS] Button is clickable! Executing click()...")
        success_btn.click()

        # ----------------------------------------------------------------------
        # 2. Visibility Wait & Text Assertion
        # ----------------------------------------------------------------------
        print("[INFO] Waiting for success alert element to become visible...")
        alert_locator = (By.CSS_SELECTOR, ".alert-success")
        alert_element = wait.until(EC.visibility_of_element_located(alert_locator))
        
        alert_text = alert_element.text
        print(f"[SUCCESS] Alert Element Text: '{alert_text}'")
        assert "success" in alert_text.lower(), \
            f"Assertion Error! 'success' missing from alert text: '{alert_text}'"

        # ----------------------------------------------------------------------
        # 3. Performance Benchmark: time.sleep(3) vs. Explicit WebDriverWait
        # ----------------------------------------------------------------------
        print("\n--- BENCHMARK: time.sleep(3) vs. WebDriverWait ---")
        
        # Test A: Hardcoded time.sleep(3)
        driver.refresh()
        start_sleep_time = time.time()
        
        btn = driver.find_element(*success_btn_locator)
        btn.click()
        time.sleep(3)  # Hardcoded static wait
        alert = driver.find_element(*alert_locator)
        _ = alert.text
        
        elapsed_sleep_time = time.time() - start_sleep_time
        print(f"[RESULT] Hardcoded time.sleep(3) total time: {elapsed_sleep_time:.4f} seconds")

        # Test B: Explicit Dynamic WebDriverWait
        driver.refresh()
        start_explicit_time = time.time()
        
        btn_exp = wait.until(EC.element_to_be_clickable(success_btn_locator))
        btn_exp.click()
        alert_exp = wait.until(EC.visibility_of_element_located(alert_locator))
        _ = alert_exp.text
        
        elapsed_explicit_time = time.time() - start_explicit_time
        print(f"[RESULT] Dynamic Explicit Wait total time:     {elapsed_explicit_time:.4f} seconds")

        time_difference = elapsed_sleep_time - elapsed_explicit_time
        print(f"[ANALYSIS] Dynamic Explicit Wait was {time_difference:.4f} seconds FASTER!")

    finally:
        driver.quit()


"""
================================================================================
EXPLICIT WAITS vs. HARDCODED SLEEPS & EXPECTED CONDITIONS DEEP DIVE
================================================================================

1. WHY time.sleep(3) IS BAD PRACTICE:
   - Fixed Waste of Execution Time: time.sleep(3) forces the execution thread to 
     pause for 3 full seconds, even if the target DOM element renders in 50ms. 
     In a test suite with 500 tests, hardcoded sleeps add 25+ minutes of wasted execution.
   - Flakiness on Slow Environments: If a CI server is under heavy load and an element 
     takes 3.1 seconds to appear, time.sleep(3) fails immediately with an exception.
   - Explicit Wait Superiority: Dynamic explicit waits poll the DOM every 500ms and 
     resume immediately once the condition is satisfied (e.g. 80ms), providing both 
     maximum execution speed and rock-solid reliability under slow network conditions.

2. DIFFERENCE BETWEEN visibility_of_element_located AND element_to_be_clickable:
   - EC.visibility_of_element_located(locator):
     * Checks that the element is present in the DOM AND has a height and width 
       greater than 0 (i.e. display != 'none' and visibility != 'hidden').
     * Use Case: Asserting displayed text, labels, warning alerts, or status icons.

   - EC.element_to_be_clickable(locator):
     * Checks that the element is visible AND enabled (is_enabled() == True) AND 
       is NOT obscured/covered by any overlay, spinner, or modal backdrop.
     * Use Case: Interacting with submit buttons, checkboxes, dropdown menus, and links.
================================================================================
"""

if __name__ == "__main__":
    run_explicit_waits_demo()
