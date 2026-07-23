"""
================================================================================
HANDS-ON 7: POM TEST - SELECT DROPDOWN (test_dropdown.py)
================================================================================
Refactored Dropdown selection test suite using DropdownPage object.
Guarantees ZERO driver.find_element calls inside test logic.
================================================================================
"""

import pytest
from HandsOn7_PageObjectModel.pages.dropdown_page import DropdownPage


@pytest.mark.pom
@pytest.mark.parametrize("target_day", ["Monday", "Wednesday", "Friday", "Sunday"])
def test_dropdown_selection(driver, base_url, target_day: str) -> None:
    """Verifies day selection from HTML dropdown using DropdownPage methods."""
    dropdown_page = DropdownPage(driver)
    dropdown_page.navigate_to(f"{base_url}select-dropdown-demo")

    # Select day using page method
    dropdown_page.select_day(target_day)

    # Assert selected option text
    selected_option = dropdown_page.get_selected_day()
    assert selected_option == target_day, \
        f"Assertion Failed! Expected selected option '{target_day}', but got '{selected_option}'"

    # Assert feedback paragraph text
    displayed_result = dropdown_page.get_displayed_result_text()
    assert target_day in displayed_result, \
        f"Assertion Failed! Feedback paragraph '{displayed_result}' did not contain '{target_day}'"
