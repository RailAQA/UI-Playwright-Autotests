from playwright.sync_api import Page, expect
from typing import Pattern

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Sidebar icon')
        self.tittle = Text(page, f'{identifier}-drawer-list-item-title-text', 'Sidebaer tittle')
        self.button = Button(page, f'{identifier}-drawer-list-item-button')

    def check_visible(self, tittle: str):
        expect(self.icon).to_be_visible()
        
        expect(self.tittle).to_be_visible()
        expect(self.tittle).to_have_text(tittle)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)