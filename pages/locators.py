from selenium.webdriver.common.by import By
from selenium import webdriver
browser = webdriver.Chrome()


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators():
    BASKET_CLICK = (By.CSS_SELECTOR, '#add_to_basket_form')


class CheckNameLocators():
    PRODUCT_NAME_1 = (By.TAG_NAME, "h1")
    PRODUCT_NAME_2 = (By.CSS_SELECTOR, '#messages .alert:first-child strong')


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert > div > strong")


