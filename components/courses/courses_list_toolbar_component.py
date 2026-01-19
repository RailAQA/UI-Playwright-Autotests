from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.tittle = Text(page, 'courses-list-toolbar-title-text', 'Tittle')
        self.create_courses_button = Button(page, 'courses-list-toolbar-create-course-button', 'Create course')

    def check_visible(self, tittle: str):
        self.tittle.check_visible()
        self.tittle.check_have_text(tittle)

        self.create_courses_button.check_visible()
    
    def click_create_course_button(self):
        self.create_courses_button.click()
        self.check_current_url(re.compile(r'.*/#/courses/create'))