from colorsys import hsv_to_rgb

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_window():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/windows")


    parent_window = driver.current_window_handle
    print(parent_window)

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    wait.until(EC.number_of_windows_to_be(2))

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        if handle != parent_window:
            driver.switch_to.window(handle)
            wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
            assert "New Window" in driver.page_source
            print("Assertion passed")
            break

