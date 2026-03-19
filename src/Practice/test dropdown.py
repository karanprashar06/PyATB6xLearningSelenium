import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://google.com")

dropdown = Select(driver.find_element(By.NAME, "q"))
dropdown.select_by_visible_text("India")
dropdown.select_by_value("In")
dropdown.select_by_index2(2)



#get all options from drop down

options= select.options()
for option in options:
    print(option.text)

