from playwright.sync_api import Page
from pages.base_page import BasePage
import re

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = RegistrationFormComponent(page).regis_button
        self.login_button = RegistrationFormComponent(page).login_button

    def click_registration_button(self):
        self.registration_button.click()
        self.registration_form.check_current_url(re.compile(r'.*/#/dashboard'))

    def click_login_button(self):
        self.login_button.click()
        self.check_current_url(re.compile(r'.*/#/auth/login'))