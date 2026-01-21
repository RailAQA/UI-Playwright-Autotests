from playwright.sync_api import Page
import re

from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button
from elements.text import Text

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'Tittle')

        self.email = Input(page, 'registration-form-email-input', 'Email')
        self.username = Input(page, 'registration-form-username-input', 'Login input')
        self.password = Input(page, 'registration-form-password-input', 'Password input')

        self.regis_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_button = Button(page, 'registration-page-login-link', 'Login')

    def registration(self, mail:str, name: str, passwrd: str):
        self.email.fill(mail)
        self.email.check_have_value(mail)

        self.username.fill(name)
        self.username.check_have_value(name)

        self.password.fill(passwrd)
        self.password.fill(passwrd)

        self.regis_button.click()
        self.page.check_current_url(re.compile(r'.*/#/dashboard'))

    def check_visible(self):
        self.title.check_have_text('UI Course')

        self.username.check_visible()
        self.password.check_visible()
        self.regis_button.check_visible()
        self.login_button.check_visible()

    def login(self):
        self.login_button.click()
        self.check_current_url(r'.*#/auth/login')