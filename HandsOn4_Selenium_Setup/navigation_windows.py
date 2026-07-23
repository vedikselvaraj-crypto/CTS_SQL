"""
================================================================================
HANDS-ON 4 - TASK 2: WEBDRIVER NAVIGATION AND WINDOW COMMANDS
================================================================================
Demonstrates browser navigation history, multi-tab switching, screenshot 
capture, and window size management in Selenium WebDriver.
================================================================================
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def run_navigation_windows_demo() -> None:
    """Executes navigation commands (back, forward, refresh), opens and switches
    between browser tabs, captures screenshots, and adjusts window dimensions.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Create screenshots directory if it does not exist
        script_dir = os.path.dirname(os.path.abspath(__file__))
        screenshots_dir = os.path.join(script_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # ----------------------------------------------------------------------
        # 1. Navigation & URL Verification
        # ----------------------------------------------------------------------
        base_url = "https://www.lambdatest.com/selenium-playground/"
        print(f"[INFO] Navigating to Base URL: {base_url}")
        driver.get(base_url)

        print("[INFO] Clicking 'Simple Form Demo' link...")
        simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
        simple_form_link.click()

        current_url = driver.current_url
        print(f"[INFO] Current URL: {current_url}")
        assert "simple-form-demo" in current_url, \
            f"Assertion Failed! 'simple-form-demo' not in URL: {current_url}"
        print("[SUCCESS] URL assertion passed!")

        print("[INFO] Executing driver.back() navigation...")
        driver.back()
        print(f"[INFO] URL after back(): {driver.current_url}")

        print("[INFO] Executing driver.forward() navigation...")
        driver.forward()
        print(f"[INFO] URL after forward(): {driver.current_url}")

        print("[INFO] Refreshing page via driver.refresh()...")
        driver.refresh()

        # ----------------------------------------------------------------------
        # 2. Multi-Tab & Window Handle Management
        # ----------------------------------------------------------------------
        print("[INFO] Opening new browser tab via JavaScript execution...")
        driver.execute_script("window.open('https://www.google.com');")

        all_handles = driver.window_handles
        print(f"[INFO] Total Open Window Handles: {len(all_handles)}")
        print(f"[INFO] Handles List: {all_handles}")

        # Switch to newly opened tab (Index 1)
        print("[INFO] Switching to tab index 1 (Google)...")
        driver.switch_to.window(all_handles[1])
        google_title = driver.title
        print(f"[SUCCESS] Tab Index 1 Title: '{google_title}'")
        assert "Google" in google_title, "Failed to switch to Google tab!"

        # Switch back to original tab (Index 0)
        print("[INFO] Switching back to tab index 0 (Original Tab)...")
        driver.switch_to.window(all_handles[0])
        original_title = driver.title
        print(f"[SUCCESS] Tab Index 0 Title: '{original_title}'")

        # ----------------------------------------------------------------------
        # 3. Screenshot Capture
        # ----------------------------------------------------------------------
        screenshot_path = os.path.join(screenshots_dir, "playground_screenshot.png")
        driver.save_screenshot(screenshot_path)
        print(f"[SUCCESS] Screenshot saved to: {screenshot_path}")
        assert os.path.exists(screenshot_path), "Screenshot file creation failed!"

        # ----------------------------------------------------------------------
        # 4. Window Dimension Management & Responsive Rationale
        # ----------------------------------------------------------------------
        # ----------------------------------------------------------------------
        # RATIONALE FOR CONSISTENT WINDOW SIZING IN UI AUTOMATION:
        # ----------------------------------------------------------------------
        # Modern web applications use responsive CSS media queries. Running tests 
        # on different browser window dimensions can cause elements (like navigation 
        # menus) to collapse into hamburger icons or change DOM positioning, causing 
        # ElementNotInteractableException or locator failures.
        # Enforcing a fixed window resolution (e.g. 1280x800 or 1920x1080) ensures 
        # deterministic UI rendering across all developer workstations and CI nodes.
        # ----------------------------------------------------------------------
        initial_size = driver.get_window_size()
        print(f"[INFO] Initial Window Size: {initial_size}")

        print("[INFO] Setting Window Size to (1280, 800)...")
        driver.set_window_size(1280, 800)
        updated_size = driver.get_window_size()
        print(f"[SUCCESS] Updated Window Size: {updated_size}")

    finally:
        print("[INFO] Teardown: Closing all browser handles...")
        driver.quit()


if __name__ == "__main__":
    run_navigation_windows_demo()
