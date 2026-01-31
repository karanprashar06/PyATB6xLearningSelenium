import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Timeout")
@allure.description("Timeout")
def test_timeout_exception_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()

    try:
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.ID, "submit")))
        print("End of the program")
    except TimeoutException as toe:
        print(toe)
    finally:
        driver.quit()

