"""
================================================================================
HANDS-ON 7: CHECKBOX PAGE OBJECT (checkbox_page.py)
================================================================================
Encapsulates locators and user action methods for Checkbox Demo page.
Contains ZERO assertions.
================================================================================
"""

from typing import Tuple
from selenium.webdriver.common.by import By
from HandsOn7_PageObjectModel.pages.base_page import BasePage


class CheckboxPage(BasePage):
    """Page Object for LambdaTest Checkbox Demo page."""

    # --------------------------------------------------------------------------
    # CLASS-LEVEL LOCATORS
    # --------------------------------------------------------------------------
    SINGLE_CHECKBOX: Tuple[str, str] = (By.ID, "isAgeSelected")
    MULTI_CHECKBOX_BUTTON: Tuple[str, str] = (By.ID, "box")
    OPTION_CHECKBOXES: Tuple[str, str] = (By.CSS_SELECTOR, "input.cb1-element")

    def check_single_checkbox(self) -> "CheckboxPage":
        """Selects the single checkbox if not already checked."""
        if not self.is_selected(self.SINGLE_CHECKBOX):
            self.click(self.SINGLE_CHECKBOX)
        return self

    def uncheck_single_checkbox(self) -> "CheckboxPage":
        """Deselects the single checkbox if currently checked."""
        if self.is_selected(self.SINGLE_CHECKBOX):
            self.click(self.SINGLE_CHECKBOX)
        return self

    def is_single_checkbox_checked(self) -> bool:
        """Returns True if single checkbox is selected, False otherwise."""
        return self.is_selected(self.SINGLE_CHECKBOX)

    def check_option(self, index: int) -> "CheckboxPage":
        """Selects option checkbox at 1-based index (1 to 4)."""
        elements = self.find_all(self.OPTION_CHECKBOXES)
        if 1 <= index <= len(elements):
            target_elem = elements[index - 1]
            if not target_elem.is_selected():
                target_elem.click()
        return self

    def uncheck_option(self, index: int) -> "CheckboxPage":
        """Deselects option checkbox at 1-based index (1 to 4)."""
        elements = self.find_all(self.OPTION_CHECKBOXES)
        if 1 <= index <= len(elements):
            target_elem = elements[index - 1]
            if target_elem.is_selected():
                target_elem.click()
        return self

    def is_option_checked(self, index: int) -> bool:
        """Returns selection state of option checkbox at 1-based index (1 to 4)."""
        elements = self.find_all(self.OPTION_CHECKBOXES)
        if 1 <= index <= len(elements):
            return elements[index - 1].is_selected()
        return False
