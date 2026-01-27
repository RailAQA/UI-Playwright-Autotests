import pytest
import allure

from tools.allure.tags import AllureTag
from pages.authentification.login_page import LoginPage
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.suite(AllureFeature.AUTHENTIFICATION)
@allure.story(AllureStory.AUTHERIZATION)
@allure.sub_suite(AllureStory.AUTHERIZATION)
class TestLogin:
    @allure.tag('USER_LOGIN')
    @allure.severity(Severity.BLOCKER)
    @allure.title('User login with correct email and password')
    def test_successful_authorization(
            self, 
            registration_page: RegistrationPage, 
            dashboard_page: DashboardPage,
            login_page: LoginPage
            ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(
            mail='user_mail@gmail.com', 
            name='username', 
            passwrd='password123'
            )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.check_visible()
        login_page.login_form.fill(
            email='user_mail@gmail.com',
            passwrd='password123'
        )
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()

    @pytest.mark.parametrize('email, password', 
                             [
                                 ('user.name@mail.ru', 'password'),
                                 ('user@yandex.ru', '   '),
                                 ('   ', 'password')
                             ]
                             )
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    @allure.title('User login with wrong email or password')
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill(email, password)
        login_page.login_button.click()
        login_page.check_visible_wrong_email_or_password()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title('Navigate from login page to registration page')
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