from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):
    cart_tab_selector = (By.XPATH, "//a[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button_selector).click()