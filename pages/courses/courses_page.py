from playwright.sync_api import Page

from pages.base_page import BasePage
from components.courses.courses_list_toolbar_component import CoursesListToolbarComponent
from components.courses.course_view_component import CourseViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_courses_list = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)

        self.toolbar = CoursesListToolbarComponent(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

    def check_visible_empty_view(self):
        self.empty_courses_list.check_visible(
            'There is no results', 
            'Results from the load test pipeline will be displayed here'
            )
