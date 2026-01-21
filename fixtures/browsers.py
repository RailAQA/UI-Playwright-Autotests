import pytest
from playwright.sync_api import Page, Playwright

@pytest.fixture
def chromium_page(page: Playwright) -> Page:
    browser = page.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
