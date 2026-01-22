import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    page = playwright.chromium.launch(headless=False)
    yield page.new_page()
    page.close()
