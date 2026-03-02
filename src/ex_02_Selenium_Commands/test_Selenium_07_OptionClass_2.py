import allure
import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.mark.new_test
@allure.title("Selenium Test")
@allure.description("Selenium Test")
def test_broswer():
    chrome_options =Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window_size =900,600")
    driver = webdriver.Chrome(chrome_options)
    driver.get("http://google.com")
    print(driver.page_source)
    assert "Google" in driver.page_source
    time.sleep(3)

