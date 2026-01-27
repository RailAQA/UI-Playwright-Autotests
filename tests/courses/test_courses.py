import pytest
import allure

from tools.allure.tags import AllureTag
from pages.courses.courses_page import CoursesPage
from pages.courses.create_course_page import CreateCoursesPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_page_with_state : CoursesPage):
        courses_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
            )
        courses_page_with_state.check_visible_empty_view()
        courses_page_with_state.navbar.check_visible('username')
        courses_page_with_state.sidebar.check_visible()
        courses_page_with_state.sidebar.check_visible()

    @allure.title('User create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(
            self, 
            courses_page_with_state: CoursesPage, 
            create_courses_page_with_state: CreateCoursesPage
            ):
        create_courses_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
            )
        create_courses_page_with_state.navbar.check_visible('username')
        create_courses_page_with_state.sidebar.check_visible()
        create_courses_page_with_state.image_upload_widget.check_visible()
        create_courses_page_with_state.create_course_toolbar.check_visible(is_image_uploaded=False)
        create_courses_page_with_state.check_visible_image_empty_view()
        create_courses_page_with_state.exercise_toolbar.check_visible()
        create_courses_page_with_state.create_course_form.check_visible(
            title='', 
            estimated_time='', 
            description='', 
            max_score='0', 
            min_score='0'
            )
        create_courses_page_with_state.exercise_empty_view.check_visible(tittle='There is no exercises',
                                                                         description='Click on "Create exercise" button to create new exercise'
                                                                         )
        
        create_courses_page_with_state.image_upload_widget.upload_preview_image(file='./testdata/files/main.jpg')
        create_courses_page_with_state.image_upload_widget.check_visible(is_image_uploaded=True)
        create_courses_page_with_state.create_course_form.fill(
            title='Playwright', 
            estimated_time='2 days', 
            description='Здесь могла быть твоя реклама', 
            max_score='40', 
            min_score='20'
            )
        create_courses_page_with_state.create_course_toolbar.click_create_course_button()

        courses_page_with_state.toolbar.check_visible()
        courses_page_with_state.course_view.check_visible(
            index=0,
            tittle='Playwright',
            max_score='40',
            min_score='20',
            estimated_time='2 days'
        )


    @allure.title('User edit course')
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, courses_page_with_state: CoursesPage, create_courses_page_with_state: CreateCoursesPage):
        create_courses_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
            )
        
        create_courses_page_with_state.image_upload_widget.upload_preview_image(file='./testdata/files/main.jpg')
        create_courses_page_with_state.create_course_form.fill(
            title='Лучший тайтл', 
            estimated_time='2 weeks', 
            description='По щучьему велению, по моему хотению', 
            max_score='25', 
            min_score='5'
            )
        create_courses_page_with_state.create_course_toolbar.click_create_course_button()

        courses_page_with_state.menu.click_edit(index=0)
        
        create_courses_page_with_state.create_course_form.check_visible(
            title='Лучший тайтл', 
            estimated_time='2 weeks', 
            description='По щучьему велению, по моему хотению', 
            max_score='25', 
            min_score='5')
        create_courses_page_with_state.create_course_form.fill(
            title='Новый тайтл', 
            estimated_time='1 day', 
            description='лень придумывать', 
            max_score='100', 
            min_score='40'
            )
        create_courses_page_with_state.create_course_toolbar.click_create_course_button()

        courses_page_with_state.course_view.check_visible(
            index=0, 
            tittle='Новый тайтл', 
            estimated_time='1 day', 
            max_score='100', 
            min_score='40'
            )
        
        