from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     page.solve_quiz_and_get_code()
#     page1 = ProductPage(browser, browser.current_url)
#     page1.name_verification()
#     # page1.should_not_be_success_message()
#     page1.should_be_disappeared()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page1 = BasketPage(browser, browser.current_url)
    page1.we_expect_no_items_in_the_basket()
    page1.we_expect_that_there_is_text_that_the_basket_is_empty()


# def test_guest_should_see_login_link_on_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     page.should_be_disappeared()


