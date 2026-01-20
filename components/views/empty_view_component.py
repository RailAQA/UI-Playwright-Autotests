from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.icon import Icon

class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Icon')
        self.tittle = Text(page, f'{identifier}-empty-view-title-text', 'Tittle')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Description')

    def check_visible(self, tittle: str, description: str):
        self.icon.check_visible()

        self.tittle.check_visible()
        self.tittle.check_have_text(tittle)

        self.description.check_visible()
        self.description.check_have_text(description)
