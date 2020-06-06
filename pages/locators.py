from selenium.webdriver.common.by import By
from selenium import webdriver
browser = webdriver.Chrome()


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class RegisterForm:
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")


class BasketPageLocators:
    BASKET_CLICK = (By.CSS_SELECTOR, '#add_to_basket_form > button')


class CheckNameLocators:
    PRODUCT_NAME_1 = (By.TAG_NAME, "h1")
    PRODUCT_NAME_2 = (By.CSS_SELECTOR, '#messages .alert:first-child strong')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasketItems:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class ContentInner:
    CONTENT_INNER = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > div.content')

