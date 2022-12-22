import unittest

from pages.login import LoginPage
from pages.products import ProductsPage
from utils.helpers import create_driver


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver("chrome")
        self.driver.get("https://automationexercise.com/")

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)

        self.products_page.check_ads()
        self.login_page.login_with_email("seleniumremote@gmail.com", "tester")

    def test_category(self):
        self.products_page.select_category()
        self.assertTrue(self.products_page.get_visible_products())

    def test_brands(self):
        items_amount = self.products_page.select_brand()
        self.assertEqual(items_amount, len(self.products_page.get_visible_products()))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
