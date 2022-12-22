from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import BROWSER, RYANAIR_URL, TIMEOUT
from utils.helpers import create_driver


class BasePage:
    class Webdriver:

        def __init__(self):
            self.driver = create_driver(BROWSER)
            self.driver.get(RYANAIR_URL)

    driver: webdriver.Chrome = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.Webdriver().driver

    def click(self, locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
