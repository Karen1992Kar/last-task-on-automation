from .locators import CheckNameLocators
from .locators import ProductPageLocators
from .main_page import MainPage
import pytest


class ProductPage(MainPage):

    def name_verification(self):
        name_1 = self.browser.find_element(*CheckNameLocators.PRODUCT_NAME_1).text
        name_2 = self.browser.find_element(*CheckNameLocators.PRODUCT_NAME_2).text
        assert name_1 == name_2, "anunner@ havasar chen"

    @pytest.mark.xfail
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    @pytest.mark.xfail
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "element is not disappeared"
