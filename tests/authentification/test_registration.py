import pytest
from playwright.sync_api import Page, Playwright

from pages.authentification.registration_page import RegistrationPage
from pages.authentification.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage


class TestAuthorization:
    def test_succesful_registration(
            self, 
            registration_page: RegistrationPage, 
            dashboard_page: DashboardPage,
            login_page: LoginPage
            ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill('pochta_random@gmail.com', 'Rail', 'password')
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('Rail')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        # Переход на страницу авторизации и авторизация
        login_page.login_form.fill('pochta_random@gmail.com', 'password')
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.navbar.check_visible('Rail')
        dashboard_page.sidebar.check_visible()
        dashboard_page.dashboard_toolbar_view.check_visible()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
            )
        login_page.click_registration_link()
        
        registration_page.registration_form.check_visible()
