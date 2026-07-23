"""
================================================================================
HANDS-ON 7: POM TEST - CHECKBOX DEMO (test_checkbox.py)
================================================================================
Refactored Checkbox test suite using CheckboxPage object.
Guarantees ZERO driver.find_element calls inside test logic.
================================================================================
"""

import pytest
from HandsOn7_PageObjectModel.pages.checkbox_page import CheckboxPage


@pytest.mark.pom
def test_single_checkbox_toggle(driver, base_url) -> None:
    """Verifies single checkbox toggle state via CheckboxPage methods."""
    checkbox_page = CheckboxPage(driver)
    checkbox_page.navigate_to(f"{base_url}checkbox-demo")

    # Ensure starting unchecked
    checkbox_page.uncheck_single_checkbox()
    assert checkbox_page.is_single_checkbox_checked() is False, \
        "Single checkbox should be unchecked initially!"

    # Action 1: Check single checkbox
    checkbox_page.check_single_checkbox()
    assert checkbox_page.is_single_checkbox_checked() is True, \
        "Single checkbox should be checked after check_single_checkbox()!"

    # Action 2: Uncheck single checkbox
    checkbox_page.uncheck_single_checkbox()
    assert checkbox_page.is_single_checkbox_checked() is False, \
        "Single checkbox should be unchecked after uncheck_single_checkbox()!"


@pytest.mark.pom
def test_multi_option_checkboxes(driver, base_url) -> None:
    """Verifies multi-option checkbox selection via CheckboxPage methods."""
    checkbox_page = CheckboxPage(driver)
    checkbox_page.navigate_to(f"{base_url}checkbox-demo")

    # Select Option 1 (Index 1) and Option 3 (Index 3)
    checkbox_page.check_option(1)
    checkbox_page.check_option(3)

    assert checkbox_page.is_option_checked(1) is True, "Option 1 should be checked!"
    assert checkbox_page.is_option_checked(2) is False, "Option 2 should be unchecked!"
    assert checkbox_page.is_option_checked(3) is True, "Option 3 should be checked!"

    # Uncheck Option 1
    checkbox_page.uncheck_option(1)
    assert checkbox_page.is_option_checked(1) is False, "Option 1 should be unchecked after uncheck!"
