import unittest

from ryanair.pages.flights import FlightsPage
from ryanair.pages.home import HomePage


class SearchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.home_page = HomePage()
        self.flights_page = FlightsPage()

    def test_something(self):
        self.home_page.accept_cookies()
        self.home_page.set_trip_type("one-way")
        self.home_page.set_departure("LUZ")
        self.home_page.set_destination("DUB")
        self.home_page.choose_departure_date("2023-01-23")
        self.home_page.search_flights()
        self.assertGreater(len(self.flights_page.get_available_flights()), 0)

    def test_with_params(self):
        self.home_page.accept_cookies()
        self.home_page.search_flights_with_parameters("return", "LUZ", "DUB", "2023-01-23", "2023-01-23")
        self.assertGreater(len(self.flights_page.get_available_flights()), 0)


if __name__ == '__main__':
    unittest.main()
