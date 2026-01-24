import pytest
from playwright.sync_api import Playwright, Page

from pages.authentification.registration_page import RegistrationPage

@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    page = playwright.chromium.launch(headless=False)
    yield page.new_page()
    page.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill('test@mail.ru', 'username', 'password')
    registration_page.click_registration_button()

    context.storage_state(path='browser_state.json')

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser_state.json")
    yield context.new_page()
    browser.close()
