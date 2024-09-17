import os
from telnetlib import EC

import requests
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from .base_page import BasePage
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

class SbisPage(BasePage):
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    CONTACTS_SECTION = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.XPATH, '//*[@title="tensor.ru"]')
    region = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    partners = (By.CLASS_NAME, "sbisru-Contacts-List__name")
    input_region = (By.CLASS_NAME, "controls-Field")
    new_region = (By.XPATH, '//*[@title="Камчатский край"]')
    close = (By.CLASS_NAME, "sbis_ru-Region-Panel__header-close")
    download = (By.CLASS_NAME, "sbisru-Footer__link")
    filse = (By.CLASS_NAME, "sbis_ru-DownloadNew-loadLink__link")
    URL = "https://sbis.ru/"
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def open(self):
        self.driver.get(self.URL)
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def go_to_contacts(self):
        self.click_element(self.CONTACTS_SECTION)
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def click_tensor_banner(self):
        self.click_element(self.TENSOR_BANNER)
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def Region(self):
        span = self.find_elements(self.region)
        return span[0].text
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def get_partners_list(self):
        partners = self.find_elements(self.partners)
        if len(partners) >= 55:
            try:
                return partners
            except Exception as e:
                print(f"Ошибка: {str(e)}")
        else:
            print("------------")
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def change_region(self):
        span = self.find_elements(self.region)
        return span[0].click()
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def new_region(self):
        inputs = self.change_region()
        try:
            input = self.find_elements(self.input_region)
            input[0].send_keys('Камчатский край' + "\n")
            return inputs , input
        except Exception as e:
            print(f"Ошибка : {str(e)}")
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def click_new_region(self,driver):
        try:
            span = self.find_element(self.new_region)
            span.click()
            driver.refresh()
            print("Элемент успешно кликнут!")
        except Exception as e:
            print(f"Ошибка клика: {str(e)}")
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def close_region(self,driver):
        self.click_new_region(driver)
        div_close = self.find_element(self.close)
        return div_close.click()

