import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@allure.title("Timeout Exception Demo")
@allure.description("Demonstrate handling of TimeoutException when element is not found")
def test_timeout_exception_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Google homepage"):
            driver.get("https://google.com")

        with allure.step("Wait for non-existing element to trigger timeout"):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit"))
            )

        # If it reaches here, test should fail
        assert False, "TimeoutException was expected but did not occur"

    except TimeoutException:
        with allure.step("TimeoutException caught as expected"):
            assert True  # Expected behavior

    finally:
        driver.quit()