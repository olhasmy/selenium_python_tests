from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    
    browser.switch_to.alert.accept()
    
    y = calc(browser.find_element(By.ID, "input_value").text)
    
    input = browser.find_element(By.ID, "answer").send_keys(y)
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    time.sleep(10)

finally:
    browser.quit()
   
