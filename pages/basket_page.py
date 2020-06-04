from .base_page import BasePage
from .locators import BasketItems
from .locators import ContentInner


class BasketPage(BasePage):

    def we_expect_no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketItems.BASKET_ITEMS), "there is a product in the basket"

    def we_expect_that_there_is_text_that_the_basket_is_empty(self):
        assert self.is_element_present(*ContentInner.CONTENT_INNER), "Kein Text, dass der Warenkorb leer ist"

