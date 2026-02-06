from playwright.sync_api import expect
import allure

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger('TEXTAREA')

class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'textarea'

    def get_locator(self, **kwargs):
        return super().get_locator(**kwargs).locator('textarea').first
    
    def fill(self, value: str, **kwargs):
        step = f"Fill '{self.type_of}' '{self.name}' to value '{value}'"
        with allure.step(step):
            locator = self.get_locator(**kwargs)   
            logger.info(step)     
            locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        step = f"Checking that '{self.type_of}' '{self.name}' has value '{value}'"
        with allure.step(step):
            locator = self.get_locator(**kwargs)   
            logger.info(step)     
            expect(locator).to_have_value(value)
    
    def check_visible(self, **kwargs):
        step = f"Checking that '{self.type_of}' '{self.name}' is visible"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_visible()