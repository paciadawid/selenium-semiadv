import unittest

from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.login import LoginPage
from pages.products import ProductsPage
from utils.config import *
from utils.helpers import create_driver


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver(BROWSER)
        self.driver.get(BASE_URL)

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        self.products_page.check_ads()
        self.login_page.login_with_email(USER_EMAIL, USER_PASSWORD)

    def test_different_items(self):
        self.products_page.add_to_cart("men tshirt")
        self.products_page.add_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_total_prices()))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
