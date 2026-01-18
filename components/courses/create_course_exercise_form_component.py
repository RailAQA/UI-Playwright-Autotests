from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class CreateCourseExerciseFormComponent(BaseComponent):
    def delete_exercise_button(self, index: str):
        delete_exercise_button = self.page.get_by_test_id(
            f'create-course-exercise-{index}-box-toolbar-delete-exercise-button'
            )
        delete_exercise_button.click()

    def fill_create_exercise_form(self, index: str, tittle: str, description: str):
        exercise_tittle = self.page.get_by_test_id(
            f'create-course-exercise-form-title-{index}-input'
            )
        exercise_description = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{index}-input'
            )
        
        exercise_tittle.fill(tittle)
        expect(exercise_tittle).to_have_value(tittle)

        exercise_description.fill(description)
        expect(exercise_description).to_have_value(description)

    def click_create(self):
        create_button = self.page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        create_button.click()

    def check_visible(self, index: str, tittle: str, description: str):
        tittle_input = self.page.get_by_test_id(
            f'create-course-exercise-form-title-{index}-input'
            )
        description_input = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{index}-input'
            )
        subtitle = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')

        expect(tittle_input).to_be_visible()
        expect(tittle_input).to_have_value(tittle)

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f'#{index + 1} Exercise')

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

