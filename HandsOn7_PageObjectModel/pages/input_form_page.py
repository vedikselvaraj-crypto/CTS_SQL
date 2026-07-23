"""
================================================================================
HANDS-ON 7: INPUT FORM PAGE OBJECT (input_form_page.py)
================================================================================
Encapsulates locators and user action methods for Input Form Submit page.
Contains ZERO assertions.
================================================================================
"""

from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from HandsOn7_PageObjectModel.pages.base_page import BasePage


class InputFormPage(BasePage):
    """Page Object for LambdaTest Input Form Submit demo page."""

    # --------------------------------------------------------------------------
    # CLASS-LEVEL LOCATORS
    # --------------------------------------------------------------------------
    NAME_INPUT: Tuple[str, str] = (By.ID, "name")
    EMAIL_INPUT: Tuple[str, str] = (By.ID, "inputEmail4")
    PASSWORD_INPUT: Tuple[str, str] = (By.ID, "inputPassword4")
    COMPANY_INPUT: Tuple[str, str] = (By.ID, "company")
    WEBSITE_INPUT: Tuple[str, str] = (By.ID, "websitename")
    COUNTRY_DROPDOWN: Tuple[str, str] = (By.NAME, "country")
    CITY_INPUT: Tuple[str, str] = (By.ID, "inputCity")
    ADDRESS1_INPUT: Tuple[str, str] = (By.ID, "inputAddress1")
    ADDRESS2_INPUT: Tuple[str, str] = (By.ID, "inputAddress2")
    STATE_INPUT: Tuple[str, str] = (By.ID, "inputState")
    ZIP_INPUT: Tuple[str, str] = (By.ID, "inputZip")
    SUBMIT_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE: Tuple[str, str] = (By.CSS_SELECTOR, ".success-msg")

    def fill_form(
        self,
        name: str,
        email: str,
        password: str,
        company: str,
        website: str,
        country: str,
        city: str,
        address1: str,
        address2: str,
        state: str,
        zipcode: str
    ) -> "InputFormPage":
        """Fills out all fields on the input form."""
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.type_text(self.COMPANY_INPUT, company)
        self.type_text(self.WEBSITE_INPUT, website)

        # Select Country from HTML dropdown
        country_elem = self.wait_for_element(self.COUNTRY_DROPDOWN)
        select = Select(country_elem)
        try:
            select.select_by_visible_text(country)
        except Exception:
            select.select_by_value(country)

        self.type_text(self.CITY_INPUT, city)
        self.type_text(self.ADDRESS1_INPUT, address1)
        self.type_text(self.ADDRESS2_INPUT, address2)
        self.type_text(self.STATE_INPUT, state)
        self.type_text(self.ZIP_INPUT, zipcode)
        return self

    def submit_form(self) -> "InputFormPage":
        """Clicks the form submit button."""
        self.click(self.SUBMIT_BUTTON)
        return self

    def get_success_message(self) -> str:
        """Returns displayed success message after form submission."""
        return self.get_text(self.SUCCESS_MESSAGE)
