from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class CartPage(BasePage):
    cart_tab_selector = (By.XPATH, "//a[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    modal_popup_selector = (By.ID, "checkoutModal")

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button_selector).click()

    def check_if_modal_visible(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.modal_popup_selector))
