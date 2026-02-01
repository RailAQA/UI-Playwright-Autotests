import pytest
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page
from config import settings
from tools.routes import AppRoute

from pages.authentification.registration_page import RegistrationPage

@pytest.fixture()
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        settings.test_user.email, 
        settings.test_user.username, 
        settings.test_user.password)
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)

@pytest.fixture
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright, 
        test_name=request.node.name, 
        storage_state=settings.browser_state_file
        )
