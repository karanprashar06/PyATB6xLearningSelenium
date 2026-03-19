from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_bingSearch:

    def setup_method(self):
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--incognito")

    def test_search_bing(self):

        driver = webdriver.Chrome(options=self.options)
        driver.get("https://www.bing.com")

        wait = WebDriverWait(driver, 10)

        # locate search box
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "sb_form_q"))
        )

        # type keyword
        search_box.send_keys("selenium python")

        # wait for dynamic suggestions
        suggestions = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox']//li")
            )
        )

        print("Bing Suggestions:")

        for option in suggestions:
            print(option.text)

            if "selenium python tutorial" in option.text.lower():
                option.click()
                break
        time.sleep(3)
        # validation
        assert "s" in driver.title.lower()

        driver.quit()


obj = Test_bingSearch()
obj.setup_method()
obj.test_search_bing()