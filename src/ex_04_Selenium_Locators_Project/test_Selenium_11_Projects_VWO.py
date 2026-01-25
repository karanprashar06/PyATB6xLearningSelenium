import time
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Negative TC: app.vwo.com - Wrong Email/Passowrd -> Capture & verify the error message shown.")
@allure.description("To verify that the error message is shown if incorrect credentials are given.")
def test_verify_login_app_VWO():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    time.sleep(5)
    email_id = driver.find_element(By.XPATH,"//input[@id='login-username']")
    email_id.send_keys("KaranPrashar")

    time.sleep(5)

    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("wrongPassword")

    sign_in = driver.find_element(By.ID, "js-login-btn")
    sign_in.click()

    time.sleep(5)

    # Error Message validation - "Your email, password, IP address or location did not match"
    err_msg = driver.find_element(By.XPATH, "//div[@class='notification-box-description']")
    print(err_msg.text)
    assert err_msg.text == "Your email, password, IP address or location did not match"

    time.sleep(2)
    driver.quit()