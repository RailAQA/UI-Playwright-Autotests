from playwright.sync_api import Page, expect
import allure
from typing import Pattern

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.tittle = Text(page, f'{identifier}-drawer-list-item-title-text', 'Tittle')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')

    @allure.step('Check visible {tittle} list item')
    def check_visible(self, tittle: str):
        self.icon.check_visible()
        
        self.tittle.check_visible()
        self.tittle.check_have_text(tittle)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)