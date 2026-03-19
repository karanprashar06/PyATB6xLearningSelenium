from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_js():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")


    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")

    user_Name = driver.find_element(By.ID, "userName")
    driver.execute_script("arguments[0].scrollIntoView()", user_Name)

    time.sleep(5)

    kils_input = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('#kils')")
    kils_input.send_keys("Karan")

    input_box = driver.execute_script(
        "return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    input_box.send_keys("farmhouse")

    time.sleep(5)
