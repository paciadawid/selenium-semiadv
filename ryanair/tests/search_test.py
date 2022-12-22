import unittest

from ryanair.pages.home import HomePage


class SearchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.home_page = HomePage()

    def test_something(self):
        self.home_page.accept_cookies()
        self.home_page.set_trip_type("one-way")
        self.home_page.set_departure("LUZ")
        self.home_page.set_destination("DUB")


if __name__ == '__main__':
    unittest.main()
