import pytest
import allure

from tools.allure.tags import AllureTag
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.suite(AllureFeature.AUTHENTIFICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.tag(AllureTag.USER_REGISTRATION)
    @allure.severity(Severity.BLOCKER)
    @allure.title('User registration with correct email and password')
    def test_succesful_registration(
            self, 
            registration_page: RegistrationPage, 
            dashboard_page: DashboardPage
            ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(
            'pochta_random@gmail.com', 
            'Rail', 
            'password'
            )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        
        #dashboard_page.navbar.check_visible('Rail')
        #dashboard_page.sidebar.check_visible()
        #dashboard_page.sidebar.click_logout()

        # Переход на страницу авторизации и авторизация
        #login_page.login_form.fill('pochta_random@gmail.com', 'password')
        #login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        #dashboard_page.navbar.check_visible('Rail')
        #dashboard_page.sidebar.check_visible()
        #dashboard_page.dashboard_toolbar_view.check_visible()

    
