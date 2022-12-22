from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.CSS_SELECTOR, "[href='/products']")
    search_field_selector = (By.ID, "search_product")
    submit_search_selector = (By.ID, "submit_search")
    single_product_selector = (By.CLASS_NAME, "single-products")
    category_button_selector = (By.CSS_SELECTOR, ".category-products .fa-plus")
    subcategory_button_selector = (By.XPATH, "//div[@class='panel-collapse in']//a")
    brand_selector = (By.CSS_SELECTOR, ".brands-name span")
    add_to_cart_button_selector = (By.CLASS_NAME, "add-to-cart")
    overlay_add_to_cart_button_selector = (By.CSS_SELECTOR, ".overlay-content .add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")
    view_product_button_selector = (By.CLASS_NAME, "fa-plus-square")
    quantity_field_selector = (By.ID, "quantity")
    add_to_cart_product_details_selector = (By.CLASS_NAME, "cart")

    def search_product(self, product):
        self.driver.find_element(*self.products_tab_selector).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.search_field_selector)).send_keys(product)
        self.driver.find_element(*self.submit_search_selector).click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_button_selector))
        ActionChains(self.driver).scroll_to_element(element).scroll_by_amount(0, 400).perform()

    def get_visible_products(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.single_product_selector))
        return elements

    def select_category(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.category_button_selector)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.subcategory_button_selector)).click()

    def select_brand(self):
        brand = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.brand_selector))
        items_amount = int(brand.text[1:-1])
        brand.click()
        return items_amount

    def add_to_cart(self, item_name):
        self.search_product(item_name)
        single_product = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.single_product_selector))
        ActionChains(self.driver).move_to_element(single_product).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.overlay_add_to_cart_button_selector)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()

    def view_product(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.view_product_button_selector)).click()

    def add_item_with_quantity(self, item_name, quantity=1):
        self.search_product(item_name)
        self.view_product()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.quantity_field_selector))
        element.clear()
        element.send_keys(quantity)
        self.driver.find_element(*self.add_to_cart_product_details_selector).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()

    def add_items_with_dictionary(self, items_dict):
        for name, quantity in items_dict.items():
            self.add_item_with_quantity(name, quantity)
