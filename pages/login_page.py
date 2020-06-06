from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterForm


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Error Login FORM"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Error Register Form"

    def register_new_user(self, email, password):
        self.browser.find_element(*RegisterForm.EMAIL).send_keys(email)
        self.browser.find_element(*RegisterForm.PASSWORD1).send_keys(password)
        self.browser.find_element(*RegisterForm.PASSWORD2).send_keys(password)
        self.browser.find_element(*RegisterForm.REGISTRATION_SUBMIT).click()

