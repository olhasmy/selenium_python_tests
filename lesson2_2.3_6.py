from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()
    
    new_window = browser.window_handles[1]
    
    browser.switch_to.window(new_window)
    
    y = calc(browser.find_element(By.ID, "input_value").text)
    
    input = browser.find_element(By.ID, "answer").send_keys(y)
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    time.sleep(10)

finally:
    browser.quit()
   
