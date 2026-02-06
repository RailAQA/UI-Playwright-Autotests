from elements.text import Text


from components.base_component import BaseComponent


class DashboardToolbarComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.tittle = Text(page, 'dashboard-toolbar-title-text', 'Tittle')

    def check_visible(self):
        self.tittle.check_visible()
        self.tittle.check_have_text('Dashboard')
        