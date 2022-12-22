from selenium.webdriver.common.by import By

from ryanair.pages.base import BasePage


class FlightsPage(BasePage):
    flight_card_selector = (By.XPATH, "//flight-card")

    def get_available_flights(self):
        return self.get_elements(self.flight_card_selector)
