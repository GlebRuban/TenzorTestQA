import time

import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.tensor import TensorPage
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

def test_tensor_banner_and_force_in_people(driver):
    sbis_page = SbisPage(driver)
    tensor= TensorPage(driver)
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    sbis_page.open()
    sbis_page.go_to_contacts()
    assert sbis_page.Region() == "Московская обл."
    sbis_page.get_partners_list()
    sbis_page.new_region()
    try:
        sbis_page.click_new_region(driver)
        print("Прошел")
    except Exception as e:
        print(f"Ошибка : {str(e)}")
    time.sleep(2)
    sbis_page.close_region(driver)
    sbis_page.click_tensor_banner()
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
    tensor.open()
    assert tensor.check_force_in_people_block() == "Сила в людях"
    if tensor.click_more_button(driver):
        print(tensor.driver.current_url)
    else:
        print('')
# ------------------ Проверка размеров фотографий -------------------------
# --------------------------------------------------------------------------
    if tensor.check_images_have_same_size():
        print("Тест прошел")
    else:
        print("not ok ")
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------



