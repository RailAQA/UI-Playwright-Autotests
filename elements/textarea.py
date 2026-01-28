from playwright.sync_api import expect
import allure

from elements.base_element import BaseElement

class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'textarea'

    def get_locator(self, **kwargs):
        return super().get_locator(**kwargs).locator('textarea').first
    
    def fill(self, value: str, **kwargs):
        with allure.step(f"Fill '{self.type_of}' '{self.name}' to value '{value}'"):
            locator = self.get_locator(**kwargs)        
            locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        with allure.step(f"Checking that '{self.type_of}' '{self.name}' has value '{value}'"):
            locator = self.get_locator(**kwargs)        
            expect(locator).to_have_value(value)
    
    def check_visible(self, **kwargs):
        with allure.step(f"Checking that '{self.type_of}' '{self.name}' is visible"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()