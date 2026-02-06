from playwright.sync_api import expect

from elements.base_element import BaseElement

class Chart(BaseElement):
    @property
    def type_of(self) -> str:
        return 'chart'