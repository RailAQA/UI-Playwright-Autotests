from playwright.sync_api import Page

from pages.base_page import BasePage
from components.views.image_upload_widget import ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.exercise_list_toolbar_component import ExercisetToolbarComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_component import CreateCourseToolbarComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent


class CreateCoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_empty_view = EmptyViewComponent(page, 'create-course-preview')
        self.exercise_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_toolbar = CreateCourseToolbarComponent(page)
        self.create_course_exercise = CreateCourseExerciseFormComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.exercise_toolbar = ExercisetToolbarComponent(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

    def check_visible_image_empty_view(self):
        self.image_empty_view.check_visible('No image selected', 'Preview of selected image will be displayed here')