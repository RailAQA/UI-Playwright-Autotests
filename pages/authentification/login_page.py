from playwright.sync_api import Page
from pages.base_page import BasePage
import re

from components.authentication.login_form_component import LoginFormComponent
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = LoginFormComponent(page).login_button
        self.registration_button = LoginFormComponent(page).registation_button

    def click_login_button(self):
        self.login_button.click()
        self.check_current_url(re.compile(r'.*/#/dashboard'))

    def click_registration_button(self):
        self.registration_button.click()
        self.check_current_url(re.compile(r'.*/#/auth/registration'))