from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.CSS_SELECTOR, "[href='/products']")
    search_field_selector = (By.ID, "search_product")
    submit_search_selector = (By.ID, "submit_search")
    single_product_selector = (By.CLASS_NAME, "single-products")

    def search_product(self, product):
        self.driver.find_element(*self.products_tab_selector).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.search_field_selector)).send_keys(product)
        self.driver.find_element(*self.submit_search_selector).click()

    def get_visible_products(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.single_product_selector))
        return elements
