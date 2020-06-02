from .locators import CheckNameLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def name_verification(self):
        name_1 = self.browser.find_element(*CheckNameLocators.PRODUCT_NAME_1).text
        name_2 = self.browser.find_element(*CheckNameLocators.PRODUCT_NAME_2).text
        assert name_1 == name_2, "anunner@ havasar chen"

