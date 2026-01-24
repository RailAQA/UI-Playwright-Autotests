import pytest

from pages.courses.courses_page import CoursesPage


class TestCourses:
    def test_empty_courses_list(self, courses_page_with_state : CoursesPage):
        courses_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
            )
        courses_page_with_state.check_visible_empty_view()
        courses_page_with_state.navbar.check_visible('username')
        courses_page_with_state.sidebar.check_visible()
        courses_page_with_state.sidebar.check_visible()