from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class ViewsComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.icon = self.page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.tittle = self.page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = self.page.get_by_test_id(f'{identifier}-empty-view-description-text')

    def check_visible(self, tittle: str, description: str):
        expect(self.icon).to_be_visible()

        expect(self.tittle).to_be_visible()
        expect(self.tittle).to_have_text(tittle)

        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)