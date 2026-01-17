from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)