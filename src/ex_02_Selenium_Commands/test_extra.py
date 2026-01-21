import time
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com")

    time.sleep(200)   # ⏸ Keeps browser open for 20 seconds
    driver.quit()
