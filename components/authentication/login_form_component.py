from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button
from elements.text import Text

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'Tittle')

        self.username = Input(page, 'login-form-email-input', 'Login input')
        self.password = Input(page, 'login-form-password-input', 'Password input')

        self.login_button = Button(page, 'login-page-login-button', 'Auth')
        self.registation_button = Button(page, 'login-page-registration-link' , 'Registation')

    def login(self, username: str, passwrd: str):
        self.username.fill(username)
        self.username.check_have_value(username)

        self.password.fill(passwrd)
        self.password.fill(passwrd)

        self.login_button.click()
        self.page.check_current_url(re.compile(r'.*/#/dashboard'))

    def check_visible(self):
        self.title.check_have_text('UI Course')

        self.username.check_visible()
        self.password.check_visible()
        self.login_button.check_visible()
        self.registation_button.check_visible()

    def registration(self):
        self.registation_button.click()
        self.page.check_current_url(re.compile(r'.*/auth/registration'))