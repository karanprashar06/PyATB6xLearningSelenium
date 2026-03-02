import pytest
import allure
import time
import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_amazon():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--window-size=900x600")
    driver =webdriver.Chrome(options=chrome_options)
    driver.get("https://www.amazon.in")
    time.sleep(3)
    assert "amazon" in driver.page_source

    element_search = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
    element_search.send_keys("samsung s25 5g")

    element_search_button = driver.find_element(By.XPATH, "//input[@id ='nav-search-submit-button']")
    element_search_button.click()

    time.sleep(3)
    element_detail =driver.find_element(By.XPATH,"(//span[contains(text(),'Galaxy S25 5G Smartphone with Galaxy AI (Icyblue, ')])[1]")
    print(element_detail.text)

    assert element_detail.text  == "Galaxy S25 5G Smartphone with Galaxy AI (Icyblue, 12GB RAM, 256GB Storage), Snapdragon 8 Elite, 50 MP Camera with ProVisual Engine and 4000mAh Battery"

    time.sleep(3)
