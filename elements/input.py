from playwright.sync_api import expect
import allure

from elements.base_element import BaseElement

class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return 'input'
    
    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(**kwargs).locator('input').nth(nth)
    
    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f"Fill '{self.type_of}' '{self.name}' to value '{value}'"):
            locator = self.get_locator(nth, **kwargs)        
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f"Checking that '{self.type_of}' '{self.name}' has value '{value}'"):
            locator = self.get_locator(nth, **kwargs)        
            expect(locator).to_have_value(value)