"""
================================================================================
HANDS-ON 6: PYTEST TEST SUITE (test_playground.py)
================================================================================
Restructures Selenium automation scripts into pytest test cases using fixtures,
parameterization (@pytest.mark.parametrize), Select helper classes, and assertions.
================================================================================
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message: str) -> None:
    """Tests simple form message input and submission across multiple parameterized inputs.
    
    Steps:
    1. Navigate to Simple Form Demo page using session base_url.
    2. Enter message into input field.
    3. Click 'Get Checked Value' button.
    4. Verify displayed message equals expected input message.
    """
    target_url = f"{base_url}simple-form-demo"
    driver.get(target_url)

    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.visibility_of_element_located((By.ID, "user-message")))
    input_field.clear()
    input_field.send_keys(message)

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "showInput")))
    submit_button.click()

    displayed_message_elem = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    actual_text = displayed_message_elem.text

    assert actual_text == message, \
        f"Expected message '{message}', but got '{actual_text}'"


def test_checkbox_demo(driver, base_url) -> None:
    """Tests single checkbox interaction and state verification using is_selected().
    
    Steps:
    1. Navigate to Checkbox Demo page.
    2. Click single checkbox.
    3. Assert checkbox is_selected() is True.
    4. Click single checkbox again.
    5. Assert checkbox is_selected() is False.
    """
    target_url = f"{base_url}checkbox-demo"
    driver.get(target_url)

    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, "isAgeSelected")))

    # Initial state should be unselected
    if checkbox.is_selected():
        checkbox.click()

    # Step 1: Click to select
    checkbox.click()
    assert checkbox.is_selected() is True, "Checkbox should be selected after click!"

    # Step 2: Click to deselect
    checkbox.click()
    assert checkbox.is_selected() is False, "Checkbox should be deselected after second click!"


def test_dropdown_selection(driver, base_url) -> None:
    """Tests HTML <select> dropdown element interaction using Selenium Select class.
    
    Steps:
    1. Navigate to Select Dropdown List demo page.
    2. Instantiate Select wrapper on select element.
    3. Select option 'Wednesday'.
    4. Assert selected option text is 'Wednesday'.
    """
    target_url = f"{base_url}select-dropdown-demo"
    driver.get(target_url)

    wait = WebDriverWait(driver, 10)
    select_element = wait.until(EC.visibility_of_element_located((By.ID, "select-demo")))

    # Initialize Selenium Select class wrapper
    select = Select(select_element)
    
    # Select option by visible text
    target_day = "Wednesday"
    select.select_by_visible_text(target_day)

    # Verify first selected option
    selected_option = select.first_selected_option.text
    assert selected_option == target_day, \
        f"Expected dropdown selection '{target_day}', but got '{selected_option}'"

    # Also verify displayed result paragraph text
    selected_text_elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".selected-value")))
    assert target_day in selected_text_elem.text, \
        f"Result paragraph text '{selected_text_elem.text}' did not contain '{target_day}'"
