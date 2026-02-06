from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent
from components.courses.toolbar_list_component import ToolbarListComponent
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar = ToolbarListComponent(page, 'create-course', 'course')
    
    def click_create_course_button(self):
        self.toolbar.click_create_button()
        self.check_current_url(re.compile(r'.*/#/courses'))

    
    def check_visible(self, is_image_uploaded: bool = True):
        self.toolbar.check_visible(tittle='Create course', is_image_uploaded=is_image_uploaded)