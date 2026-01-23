from playwright.sync_api import Page
from pages.base_page import BasePage

from components.charts.charts_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from elements.button import Button


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarComponent(page)