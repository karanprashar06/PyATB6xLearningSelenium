import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_project_1_katalon_positive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 100)

    driver.get("https://www.instagram.com/")

    # ---------- Username ----------
    username = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    username.send_keys("karanprashar06@gmail.com")

    # ---------- Password ----------
    password = wait.until(EC.visibility_of_element_located((By.NAME, "pass")))
    password.send_keys("Akshay@06")

    # ---------- Login Button ----------
    login_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
    )
    login_btn.click()

    # ---------- Save Info (optional popup) ----------
    # try:
    #     save_info = wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save info']"))
    #     )
    #     save_info.click()
    # except TimeoutException:
    #     print("Save Info popup not shown")

    # ---------- Turn On Notifications (optional) ----------
    try:
        not_now = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Not Now']"))
        )
        not_now.click()
    except TimeoutException:
        print("Notification popup not shown")

    # ---------- Messages SVG ----------
    messages_icon = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[local-name()='svg' and @aria-label='Messages']")
        )
    )

    # SVGs sometimes need JS click
    driver.execute_script("arguments[0].click();", messages_icon)

    time.sleep(10)
    # driver.quit()
