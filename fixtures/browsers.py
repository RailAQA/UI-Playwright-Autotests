import pytest
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest
import allure

from pages.authentification.registration_page import RegistrationPage

@pytest.fixture()
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    page = playwright.chromium.launch(headless=False)
    context = page.new_context(record_video_dir='./videos')
    context.tracing.start(
        screenshots=True, 
        snapshots=True, 
        sources=True
        )
    page = context.new_page()
    yield page
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    page.close()
    allure.attach.file(source=f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(source=page.video.path(), name='video', extension=allure.attachment_type.WEBM)

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
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser_state.json", record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()
    allure.attach.file(source=f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(source=page.video.path(), name='video', extension=allure.attachment_type.WEBM)
