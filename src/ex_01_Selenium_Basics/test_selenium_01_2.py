import pytest
import allure
import selenium
from selenium import webdriver

@allure.title("Verify that we are able to open page using Selenium")
@allure.description("Verify that we are able to open page using Selenium")
@pytest.mark.selenium_01
def test_01():
    driver= webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)
    assert driver.title == "Google"