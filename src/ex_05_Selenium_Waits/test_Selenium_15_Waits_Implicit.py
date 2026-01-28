import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("app.vwo.com - Implicit Wait")
@allure.description("To verify that the app.vwo.com is loaded with implicit wait.")
def test_implicit_wait():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(5)

    email = driver.find_element(By.XPATH, "//input[@name='username']")
    email.send_keys("karanprashar06@gmail.com")

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("flvcafdl")

    login = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    login.click()

    time.sleep(5)

    #err_message = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    # partial text
    #err_message = driver.find_element(By.XPATH, "//div[contains(text(), 'did not match')]")
    #Full twxt matched
    err_message = driver.find_element(By.XPATH, "//div[normalize-space()='Your email, password, IP address or location did not match']")
    print(err_message.text)
    assert err_message.text == "Your email, password, IP address or location did not match"


    driver.implicitly_wait(3)
    driver.quit()