from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.textarea import Textarea
from elements.input import Input

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Input')
        self.estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Input')
        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'Textarea')
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Input')
        self.min_scrore_input = Input(page, 'create-course-form-min-score-input', 'Input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.fill(description)
        self.description_textarea.check_have_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_have_value(max_score)

        self.min_scrore_input.fill(min_score)
        self.min_scrore_input.check_have_value(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(max_score)

        self.min_scrore_input.check_visible()
        self.min_scrore_input.check_have_value(min_score)