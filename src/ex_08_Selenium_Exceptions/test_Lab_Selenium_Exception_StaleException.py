
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

@allure.title("Selenium exceptions")
@allure.description("Selenium exception description")
def test_selenium_exception():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    try:
        element = driver.find_element(By.NAME, "q")
        driver.refresh()
        element.send_keys("selenium")
    except StaleElementReferenceException as see:
        print(see.msg)
    time.sleep(5)

