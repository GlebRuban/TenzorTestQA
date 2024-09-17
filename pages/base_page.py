from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

class BasePage:

    def __init__(self, driver):
        self.driver = driver
# --------------------------------------------------------------------------
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
# --------------------------------------------------------------------------
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
# --------------------------------------------------------------------------
    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()