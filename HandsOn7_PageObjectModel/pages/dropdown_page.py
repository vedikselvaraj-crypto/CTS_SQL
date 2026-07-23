"""
================================================================================
HANDS-ON 7: DROPDOWN PAGE OBJECT (dropdown_page.py)
================================================================================
Encapsulates locators and user action methods for Select Dropdown List page.
Uses Selenium Select class internally. Contains ZERO assertions.
================================================================================
"""

from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from HandsOn7_PageObjectModel.pages.base_page import BasePage


class DropdownPage(BasePage):
    """Page Object for LambdaTest Select Dropdown List demo page."""

    # --------------------------------------------------------------------------
    # CLASS-LEVEL LOCATORS
    # --------------------------------------------------------------------------
    SELECT_DROPDOWN: Tuple[str, str] = (By.ID, "select-demo")
    SELECTED_VALUE_DISPLAY: Tuple[str, str] = (By.CSS_SELECTOR, ".selected-value")

    def select_day(self, day_name: str) -> "DropdownPage":
        """Selects a day from the HTML dropdown list using Selenium Select class."""
        select_element = self.wait_for_element(self.SELECT_DROPDOWN)
        select = Select(select_element)
        select.select_by_visible_text(day_name)
        return self

    def get_selected_day(self) -> str:
        """Returns the currently selected option visible text."""
        select_element = self.wait_for_element(self.SELECT_DROPDOWN)
        select = Select(select_element)
        return select.first_selected_option.text

    def get_displayed_result_text(self) -> str:
        """Returns the feedback paragraph text string."""
        return self.get_text(self.SELECTED_VALUE_DISPLAY)
