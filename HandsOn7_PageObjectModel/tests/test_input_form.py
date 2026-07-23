"""
================================================================================
HANDS-ON 7: POM TEST - INPUT FORM SUBMIT (test_input_form.py)
================================================================================
Input Form submission test suite using InputFormPage object.
Guarantees ZERO driver.find_element calls inside test logic.
================================================================================
"""

import pytest
from HandsOn7_PageObjectModel.pages.input_form_page import InputFormPage


@pytest.mark.pom
def test_input_form_submit(driver, base_url) -> None:
    """Verifies complete Input Form submission using InputFormPage methods."""
    input_form_page = InputFormPage(driver)
    input_form_page.navigate_to(f"{base_url}input-form-demo")

    # Fill form fields via page object method
    input_form_page.fill_form(
        name="Automation Lead",
        email="qa.architect@example.com",
        password="SecurePassword123!",
        company="Digital Nurture 5.0",
        website="https://www.example.com",
        country="United States",
        city="San Francisco",
        address1="100 Technology Way",
        address2="Suite 500",
        state="California",
        zipcode="94105"
    )

    # Submit form
    input_form_page.submit_form()

    # Retrieve success message and assert
    success_text = input_form_page.get_success_message()
    print(f"[INFO] Input Form Success Message: '{success_text}'")

    assert "Thanks for contacting us" in success_text, \
        f"Assertion Failed! Expected success message not found in: '{success_text}'"
