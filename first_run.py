from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, ".logo img")
driver.find_element(By.XPATH, "//div[contains(@class, 'logo')]//img")
driver.find_element(By.XPATH, "//a[@href='/view_cart']")
driver.find_element(By.ID, "susbscribe_email")
driver.find_element(By.CSS_SELECTOR, ".right.control-carousel")
driver.find_element(By.XPATH, "//div[@class='brands_products']/h2")
driver.find_element(By.ID, "footer")
driver.find_element(By.ID, "scrollUp")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='brands_products']/h2")))

driver.quit()
