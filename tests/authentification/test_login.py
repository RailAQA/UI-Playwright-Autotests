import pytest
from playwright.sync_api import Page, Playwright

from pages.authentification.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
class TestLogin:
    @pytest.mark.parametrize('email, password', 
                             [
                                 ('user.name@mail.ru', 'password'),
                                 ('user@yandex.ru', '   '),
                                 ('   ', 'password')
                             ]
                             )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill(email, password)
        login_page.login_button.click()
        login_page.check_visible_wrong_email_or_password()