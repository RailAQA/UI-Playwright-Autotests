from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.chart import Chart

class ChartViewComponent(BaseComponent):
    def __init__(self, page, identifier: str, chart_type: str):
        super().__init__(page)

        self.tittle = Text(page, f'{identifier}-widget-title-text', 'Tittle')
        self.chart_view = Chart(page, f'{identifier}-{chart_type}-chart', 'Chart')

    def check_visible(self, title):
        self.tittle.check_visible()
        self.tittle.check_have_text(title)

        self.chart_view.check_visible()