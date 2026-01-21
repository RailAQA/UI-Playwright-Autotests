from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = Page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def refresh_page(self):
        self.page.reload(wait_until='networkidle')