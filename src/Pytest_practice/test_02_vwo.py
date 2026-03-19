from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class Test_VwoLogin:

    # def setup_method(self):
    #     self.options = Options()
    #     # self.options.add_argument('--headless')
    #     self.options.add_argument('--incognito')
    #     self.options.add_argument('--start-maximized')

    def test_vwo(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://app.vwo.com/#/login")

        wait = WebDriverWait(driver, 5)


        # wait for search box
        heading = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='js-sign-in-heading']"))
        )
        print(heading.text)
        assert heading.text  == "Sign in to VWO platform"


        driver.quit()


new_obj = Test_VwoLogin()
new_obj.setup_method()
new_obj.test_vwo()