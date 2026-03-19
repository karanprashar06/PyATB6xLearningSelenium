


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException
from selenium.webdriver.common.keys import Keys

def test_selenium_exceptions():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://google.com")
    try:
        element = driver.find_element(By.ID, "no such element")

    except NoSuchElementException as NSE:
        print(NSE.msg)

