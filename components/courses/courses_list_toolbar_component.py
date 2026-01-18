from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent

class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.tittle = self.page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = self.page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible(self, tittle: str):
        expect(self.tittle).to_be_visible()
        expect(self.tittle).to_have_text(tittle)

        expect(self.create_courses_button).to_be_visible()
    
    def click_create_course_button(self):
        self.create_courses_button.click()
        self.check_current_url(re.compile(r'.*/#/courses/create'))