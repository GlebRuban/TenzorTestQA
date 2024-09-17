from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from pages.base_page import BasePage
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
class TensorPage(BasePage):
    FORCE_IN_PEOPLE_BLOCK = (By.CLASS_NAME, "tensor_ru-Index__card-title")
    MORE_BUTTON = (By.CLASS_NAME, "tensor_ru-link")
    CHRONOLOGY_IMAGES = (By.CLASS_NAME, "tensor_ru-About__block3-image")
    URL = "https://tensor.ru/"
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
    def check_force_in_people_block(self):
        p = self.find_elements(self.FORCE_IN_PEOPLE_BLOCK)
        return p[1].text
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def click_more_button(self, driver):
        a =  self.find_elements(self.MORE_BUTTON)
        if len(a) >= 3:
            try:
                driver.execute_script("document.querySelector('.preload-overlay').style.display = 'none';")
                a[1].click()
                print("Элемент успешно кликнут!")
            except Exception as e:
                print(f"Ошибка клика: {str(e)}")
        else:
            print("Error")
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def get_chronology_images(self):
        img = self.find_elements(self.CHRONOLOGY_IMAGES)
        return img
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    def check_images_have_same_size(self):
        try:
            images = self.get_chronology_images()
            sizes = [(image.size['height'], image.size['width']) for image in images]
            print("Успешно !")
            return all(size == sizes[0] for size in sizes)
        except Exception as e:
            print(f"Ошибка : {str(e)}")
