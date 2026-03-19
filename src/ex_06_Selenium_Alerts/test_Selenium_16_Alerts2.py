import pytest
import allure
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@allure.title("JavaScript Alerts")
@allure.description("time to use alert")
@pytest.mark.test_case()
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    click_JS_element = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    click_JS_element.click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()


    result_text = driver.find_element(By.XPATH,"//p[@id='result']").text
    assert result_text == "You successfully clicked an alert"
    time.sleep(5)

    # driver.implicitly_wait(10)

#xpath1 : //button[onclick='jsAlert()']   and //button[contains(text(),"Click for JS Alert")]
#xpath2 : //button[onclick='jsConfirm()']
#xpath2 : //button[onclick='Prompt()']
