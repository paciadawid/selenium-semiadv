from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa


class BasePage:

    product_tab_selector = (By.CSS_SELECTOR, "[href='/products']")
    search_product_selector = (By.ID, "search_product")
    iframe1_ads_selector = (By.XPATH, "/html/ins//iframe[contains(@name, 'swift')]")
    iframe2_ads_name = "ad_iframe"
    dismiss_button_selector = (By.ID, "dismiss-button")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def check_ads(self):
        self.driver.find_element(*self.product_tab_selector).click()
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.search_product_selector)).click()
        except TimeoutException:
            iframe = self.driver.find_element(*self.iframe1_ads_selector)
            self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame(self.iframe2_ads_name)
            self.driver.find_element(*self.dismiss_button_selector).click()
            self.driver.switch_to.parent_frame()
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.search_product_selector)).click()
