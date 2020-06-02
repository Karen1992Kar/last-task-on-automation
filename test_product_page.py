from pages.main_page import MainPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.solve_quiz_and_get_code()
    page1 = ProductPage(browser, browser.current_url)
    page1.name_verification()


