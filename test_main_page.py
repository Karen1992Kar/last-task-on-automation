from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page1 = BasketPage(browser, browser.current_url)
    page1.we_expect_no_items_in_the_basket()
    page1.we_expect_that_there_is_text_that_the_basket_is_empty()
    #time.sleep(60)


# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_login_link()          # выполняем метод страницы - переходим на страницу логина
#     page.go_to_login_page()             # откроем страницу логин
#     page1 = LoginPage(browser, browser.current_url)
#     page1.should_be_login_page()
#     time.sleep(5)

