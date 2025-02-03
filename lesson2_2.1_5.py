from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()
    
    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()
    
    
    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    btn.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
