from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_link()          # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page()             # откроем страницу логин
    page1 = LoginPage(browser, browser.current_url)
    page1.should_be_login_page()
    time.sleep(5)

