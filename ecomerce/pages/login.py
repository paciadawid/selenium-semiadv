from selenium.webdriver.common.by import By

from ecomerce.pages.base import BasePage

from selenium.webdriver.support import expected_conditions as EC  # noqa


class LoginPage(BasePage):
    login_tab_selector = (By.XPATH, "//a[@href='/login']")
    email_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.XPATH, "//input[@data-qa='login-password']")
    login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")

    def login_with_email(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.login_button_selector).click()

