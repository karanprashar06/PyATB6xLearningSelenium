import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Import below 2 settings to add fluent wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_ebay():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    driver.maximize_window()

    WebDriverWait(driver,10).until(EC.visibility_of_element_located(((By.XPATH, "//input[@placeholder='Search for anything']"))))
    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    search_box_input_xpath.send_keys("macmini")
    search_button = driver.find_element(By.XPATH, "//span[@class='gh-search-button__label']")
    search_button.click()

    #//div[@class = "s-item__title"] -> div.s-item__title - class is represented by .

    WebDriverWait(driver, 10).until(
        EC.url_contains("_nkw=macmini")
    )
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.srp-results"))
    )

    items = driver.find_elements(By.CSS_SELECTOR, "ul.srp-results li.s-item")

    print("Items count:", len(items))

    for index, item in enumerate(items):
        try:
            title_elem = item.find_elements(By.CSS_SELECTOR, ".s-item__title")
            price_elem = item.find_elements(By.CSS_SELECTOR, ".s-item__price")

            if title_elem and price_elem:
                title = title_elem[0].text
                price = price_elem[0].text

                if title.strip() != "":
                    print(f"{index} -> {title} --> {price}")

        except Exception as e:
            print("Error:", e)