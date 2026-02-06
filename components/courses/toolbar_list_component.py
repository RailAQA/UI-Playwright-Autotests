from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class ToolbarListComponent(BaseComponent):
    def __init__(self, page: Page, identifier, type):
        super().__init__(page)

        self.tittle = Text(page, f'{identifier}-toolbar-title-text', 'Tittle')
        self.button = Button(page, f'{identifier}-toolbar-create-{type}-button', 'Create button')

    def check_visible(self, tittle: str, is_image_uploaded: bool = True):
        self.tittle.check_visible()
        self.tittle.check_have_text(tittle)

        if is_image_uploaded:
            self.button.check_visible()
        else:
            self.button.check_disabled()
    
    def click_create_button(self):
        self.button.click()