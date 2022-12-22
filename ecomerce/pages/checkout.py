from selenium.webdriver.common.by import By

from ecomerce.pages.base import BasePage


class CheckoutPage(BasePage):
    total_price_selector = (By.CLASS_NAME, "cart_total_price")

    def get_total_prices(self):
        price_list = []
        price_elements = self.driver.find_elements(*self.total_price_selector)
        for price_element in price_elements[:-1]:
            price_list.append(int(price_element.text.split()[-1]))
        return price_list

    def get_total_amount(self):
        price_elements = self.driver.find_elements(*self.total_price_selector)
        total_amount = int(price_elements[-1].text.split()[-1])
        return total_amount
