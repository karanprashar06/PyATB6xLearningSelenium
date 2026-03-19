from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_spicejet():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    chrome_options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.geolocation": 2}
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.spicejet.com/")
    time.sleep(15)

    from_city = driver.find_element(By.XPATH, "//input[@value='Delhi (DEL)']")
    actions = ActionChains(driver)
    (
        actions.move_to_element(from_city)
        .click().send_keys_to_element(from_city,"blr")
        .perform()
    )
    time.sleep(5)

    To_city = driver.find_element(By.XPATH, "//div[text()='To']")
    actions = ActionChains(driver)
    (
        actions.move_to_element(To_city)
        .click().send_keys_to_element(To_city,"del")
        .perform()
    )
    time.sleep(5)

