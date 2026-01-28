from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent
from components.courses.toolbar_list_component import ToolbarListComponent


class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar = ToolbarListComponent(page, 'courses-list', 'course')
    
    def click_create_course_button(self):
        self.toolbar.click_create_button()
        self.check_current_url(re.compile(r'.*/#/courses/create'))

    def check_visible(self):
        self.toolbar.check_visible('Courses')