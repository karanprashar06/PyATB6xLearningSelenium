from selenium import webdriver
import pytest
import allure

@allure.title("Print the page source of the page")
def test_page_source():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    pageSource = driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert "CURA Healthcare Service" in pageSource

    driver.close()