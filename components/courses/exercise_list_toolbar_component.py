from playwright.sync_api import Page, expect
import re

from components.base_component import BaseComponent
from components.courses.toolbar_list_component import ToolbarListComponent
from elements.text import Text
from elements.button import Button

class ExercisetToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar = ToolbarListComponent(page, 'create-course-exercises-box', 'exercise')
    
    def click_create_exercise_button(self):
        self.toolbar.click_create_button()

    def check_visible(self):
        self.toolbar.check_visible('Exercises')