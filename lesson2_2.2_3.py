from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    total = num1+ num2

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))

    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    btn.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
