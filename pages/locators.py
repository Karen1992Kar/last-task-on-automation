from selenium.webdriver.common.by import By
from selenium import webdriver
browser = webdriver.Chrome()


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_CLICK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span')


class CheckNameLocators:
    PRODUCT_NAME_1 = (By.TAG_NAME, "h1")
    PRODUCT_NAME_2 = (By.CSS_SELECTOR, '#messages .alert:first-child strong')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert > div > strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketItems:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class ContentInner:
    CONTENT_INNER = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > div.content')

