from ecomerce.pages.products import ProductsPage
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")

        self.products_page = ProductsPage(self.driver)
        self.check_ads()

    def test_unicorn(self):
        self.products_page.search_product("unicorn")
        self.assertGreaterEqual(len(self.products_page.get_visible_products()), 2)

    def tearDown(self) -> None:
        self.driver.quit()

    def check_ads(self):
        self.driver.find_element(By.CSS_SELECTOR, "[href='/products']").click()
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.ID, "search_product"))).click()
        except TimeoutException:
            iframe = self.driver.find_element(By.XPATH, "/html/ins//iframe[contains(@name, 'swift')]")
            self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ad_iframe")
            self.driver.find_element(By.ID, "dismiss-button").click()
            self.driver.switch_to.parent_frame()
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, "search_product"))).click()
