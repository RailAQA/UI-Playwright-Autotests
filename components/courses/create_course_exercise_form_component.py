from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text

class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.tittle_exercise_input = Input(page, 'create-course-exercise-form-title-{index}-input', 'Tittle')
        self.description_input = Input(page, 'create-course-exercise-form-description-{index}-input', 'Description')
        self.subtitle = Text(page, 'create-course-exercise-{index}-box-toolbar-subtitle-text', 'Subtitle')

        self.delete_button = Button(page, 'create-course-exercise-{index}-box-toolbar-delete-exercise-button', 'Delete exercise')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create exercise')

    def delete_exercise_button(self, index: str):
        self.delete_button.click(index=index)

    def fill(self, index: str, tittle: str, description: str):
        self.tittle_exercise_input.fill(tittle, index=index)
        self.tittle_exercise_input.check_have_value(tittle, index=index)

        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description)

    def click_create(self):
        self.create_exercise_button.click()

    def check_visible(self, index: str, tittle: str, description: str):
        self.tittle_exercise_input.check_visible(index=index)
        self.tittle_exercise_input.check_have_value(tittle, index=index)

        self.subtitle.check_visible(index=index)
        self.subtitle.check_have_text(text=f'#{index + 1} Exercise', index=index)

        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(value=description, index=index)

