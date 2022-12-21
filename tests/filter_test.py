import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    login_tab_selector = (By.XPATH, "//a[@href='/login']")
    email_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.XPATH, "//input[@data-qa='login-password']")
    login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")
    category_button_selector = (By.CSS_SELECTOR, ".category-products .fa-plus")
    subcategory_button_selector = (By.XPATH, "//div[@class='panel-collapse in']//a")
    single_product_selector = (By.CLASS_NAME, "single-products")
    brand_selector = (By.CSS_SELECTOR, ".brands-name span")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")
        self.check_ads()
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys("seleniumremote@gmail.com")
        self.driver.find_element(*self.password_field_selector).send_keys("tester")
        self.driver.find_element(*self.login_button_selector).click()

    def test_category(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.category_button_selector)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.subcategory_button_selector)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.single_product_selector))

    def test_brands(self):
        brand = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.brand_selector))
        items_amount = int(brand.text[1:-1])
        brand.click()
        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.single_product_selector))
        self.assertEqual(items_amount, len(products))

    def tearDown(self) -> None:
        self.driver.quit()

    def check_ads(self):
        self.driver.find_element(By.CSS_SELECTOR, "[href='/products']").click()
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.ID, "search_product"))).send_keys(
                "unicorn")
        except TimeoutException:
            iframe = self.driver.find_element(By.XPATH, "/html/ins//iframe[contains(@name, 'swift')]")
            self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ad_iframe")
            self.driver.find_element(By.ID, "dismiss-button").click()
            self.driver.switch_to.parent_frame()
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, "search_product"))).send_keys(
                "unicorn")


if __name__ == '__main__':
    unittest.main()
