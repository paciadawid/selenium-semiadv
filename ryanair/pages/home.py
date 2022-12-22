from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from ryanair.pages.base import BasePage


class HomePage(BasePage):
    accept_cookie_button_selector = (By.XPATH, "//button[@data-ref='cookie.accept-all']")
    return_trip_button_selector = (By.XPATH, "//fsw-trip-type-button[@data-ref='flight-search-trip-type__return-trip']")
    one_way_trip_button_selector = (
    By.XPATH, "//fsw-trip-type-button[@data-ref='flight-search-trip-type__one-way-trip']")
    departure_field_selector = (By.XPATH, "//fsw-input-button[uniqueid='departure']")
    destination_field_selector = (By.XPATH, "//fsw-input-button[uniqueid='destination']")

    airport_selector = (By.XPATH, "//span[@data-id='{airport_code}']")
    departure_input_selector = (By.ID, "input-button__departure")
    destination_input_selector = (By.ID, "input-button__destination")

    def accept_cookies(self):
        self.click(self.accept_cookie_button_selector)

    def set_trip_type(self, trip_type="one-way"):
        if trip_type == "one-way":
            self.click(self.one_way_trip_button_selector)
        elif trip_type == "return":
            self.click(self.return_trip_button_selector)
        else:
            raise "Not supported trip type, choose between 'one-way' and 'return'"

    def set_departure(self, airport_code):
        try:
            self.click((self.airport_selector[0], self.airport_selector[1].format(airport_code=airport_code)), 1)
        except TimeoutException:
            self.click(self.departure_input_selector)
            self.click((self.airport_selector[0], self.airport_selector[1].format(airport_code=airport_code)))

    def set_destination(self, airport_code):
        try:
            self.click((self.airport_selector[0], self.airport_selector[1].format(airport_code=airport_code)), 1)
        except TimeoutException:
            self.click(self.destination_input_selector)
            self.click((self.airport_selector[0], self.airport_selector[1].format(airport_code=airport_code)))
