from playwright.sync_api import Page
from pages.base_page import BasePage
import allure
import re

from components.authentication.login_form_component import LoginFormComponent
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.text import Text


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = LoginFormComponent(page).login_button
        self.registration_button = LoginFormComponent(page).registation_button

        self.wrong_email_or_password_alert = Text(page, 'login-page-wrong-email-or-password-alert', 'Alert')

    def click_login_button(self):
        self.login_button.click()
        self.check_current_url(re.compile(r'.*/#/dashboard'))

    def click_registration_link(self):
        self.registration_button.click()
        self.check_current_url(re.compile(r'.*/#/auth/registration'))

    @allure.step('Check visible wrong email or password alert')
    def check_visible_wrong_email_or_password(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')