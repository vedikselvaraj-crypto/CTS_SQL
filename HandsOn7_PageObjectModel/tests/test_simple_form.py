"""
================================================================================
HANDS-ON 7: POM TEST - SIMPLE FORM (test_simple_form.py)
================================================================================
Refactored Simple Form submission test suite using SimpleFormPage object.
Guarantees ZERO driver.find_element calls inside test logic.
================================================================================
"""

import pytest
from HandsOn7_PageObjectModel.pages.simple_form_page import SimpleFormPage


@pytest.mark.pom
@pytest.mark.parametrize("input_message", ["Hello Selenium", "Page Object Model", "POM Test 2026"])
def test_simple_form_submission(driver, base_url, input_message: str) -> None:
    """Refactored Simple Form test verifying message input & submission via POM.
    
    Rule Check: ZERO driver.find_element calls exist in this test file.
    All UI interactions are delegated to SimpleFormPage methods.
    Assertions exist ONLY in test functions.
    """
    simple_form_page = SimpleFormPage(driver)
    
    # 1. Navigate using page method
    simple_form_page.navigate_to(f"{base_url}simple-form-demo")

    # 2. Execute business user actions via page methods
    simple_form_page.enter_message(input_message)
    simple_form_page.click_submit()

    # 3. Retrieve result string and assert in test
    displayed_text = simple_form_page.get_displayed_message()
    
    assert displayed_text == input_message, \
        f"Assertion Failed! Expected displayed message '{input_message}', but got '{displayed_text}'"
