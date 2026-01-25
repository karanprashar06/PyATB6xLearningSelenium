import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_vwo_LoginPage_Negativecase():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")

    time.sleep(5)

    #<input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # vwo-html-translate-attr="placeholder"
    # vwo-html-translate-placeholder="login:enterEmailID"
    # id="login-username"
    # data-qa="hocewoqisi"
    # placeholder="Enter email ID">

    input_username = driver.find_element(By.ID, "login-username")
    input_username.send_keys("karan")
    time.sleep(2)
    #<input type="password"
    # class="text-input W(100%)"
    # vwo-html-translate-attr="placeholder"
    # vwo-html-translate-placeholder="login:enterPassword"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # placeholder="Enter password">

    input_password = driver.find_element(By.ID, "login-password")
    input_password.send_keys("Wrong password")
    time.sleep(2)

    Submit_button = driver.find_element(By.ID, "js-login-btn")
    Submit_button.click()
    time.sleep(5)

    assert driver.current_url == "https://app.vwo.com/#/login"
    assert driver.title == "Login - VWO"
    print(driver.title)

    fail_message = driver.find_element(By.ID, "js-notification-box-msg")
    print(fail_message.text)
    assert "Your email, password, IP address or location did not match" == fail_message.text

    driver.quit()
