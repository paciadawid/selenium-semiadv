import unittest

from ecomerce.pages.cart import CartPage
from ecomerce.pages.checkout import CheckoutPage
from ecomerce.pages.login import LoginPage
from ecomerce.pages.products import ProductsPage
from utils.config import *
from utils.helpers import create_driver


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver(BROWSER)
        self.driver.get(BASE_URL)

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        self.products_page.check_ads()

    def test_different_items(self):
        self.login_page.login_with_email(USER_EMAIL, USER_PASSWORD)
        self.products_page.add_to_cart("men tshirt")
        self.products_page.add_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_total_prices()))

    def test_checkout_unlogged_user(self):
        self.products_page.add_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.cart_page.check_if_modal_visible()

    def test_multiple_items(self):
        self.login_page.login_with_email(USER_EMAIL, USER_PASSWORD)
        self.products_page.add_item_with_quantity("unicorn", 10)
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_total_prices()))

    def test_product_dictionary(self):
        self.login_page.login_with_email(USER_EMAIL, USER_PASSWORD)
        product_dict = {
            "unicorn": 10,
            "dress": 20,
            "tshirt": 30
        }
        self.products_page.add_items_with_dictionary(product_dict)
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_total_prices()))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
