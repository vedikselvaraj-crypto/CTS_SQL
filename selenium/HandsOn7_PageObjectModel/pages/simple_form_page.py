"""
================================================================================
HANDS-ON 7: SIMPLE FORM PAGE OBJECT (simple_form_page.py)
================================================================================
Encapsulates locators and user action methods for Simple Form Demo page.
Contains ZERO assertions.
================================================================================
"""

from typing import Tuple
from selenium.webdriver.common.by import By
from HandsOn7_PageObjectModel.pages.base_page import BasePage


class SimpleFormPage(BasePage):
    """Page Object for LambdaTest Simple Form Demo page."""

    # --------------------------------------------------------------------------
    # CLASS-LEVEL LOCATORS (Tuples: By strategy, Value)
    # --------------------------------------------------------------------------
    MESSAGE_INPUT: Tuple[str, str] = (By.ID, "user-message")
    SUBMIT_BUTTON: Tuple[str, str] = (By.ID, "showInput")
    DISPLAYED_MESSAGE: Tuple[str, str] = (By.ID, "message")

    def enter_message(self, text: str) -> "SimpleFormPage":
        """Enters text into the single message input field."""
        self.type_text(self.MESSAGE_INPUT, text)
        return self

    def click_submit(self) -> "SimpleFormPage":
        """Clicks the 'Get Checked Value' submit button."""
        self.click(self.SUBMIT_BUTTON)
        return self

    def get_displayed_message(self) -> str:
        """Returns the text string displayed in the result area after submission."""
        return self.get_text(self.DISPLAYED_MESSAGE)
