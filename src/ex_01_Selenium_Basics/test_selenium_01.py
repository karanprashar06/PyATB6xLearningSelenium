from selenium import webdriver
import allure
import pytest

@pytest.mark.postive_testcase
@allure.title("Verify that we are able to open page using Selenium")
@allure.description("Verify that we are able to open page using Selenium")
def test_selenium_01():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)
    assert driver.title == "Google"