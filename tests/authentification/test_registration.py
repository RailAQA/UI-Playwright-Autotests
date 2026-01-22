from playwright.sync_api import Page, Playwright

from pages.authentification.registration_page import RegistrationPage


def test_registration(registration_page: RegistrationPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill('bublik0706@gmail.com', 'Rail', 'password')
