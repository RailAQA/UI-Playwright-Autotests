from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text

class NavbarComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.navbar_title = Text(page, 'navigation-navbar-app-title-text', 'Navbar tittle')
        self.welcome_tittle = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome tittle')

    def check_visible(self, username: str):
        self.navbar_title.check_visible()
        self.navbar_title.check_have_text('UI Course')

        self.welcome_tittle.check_visible()
        self.welcome_tittle.check_have_text(f'Welcome, {username}!')
