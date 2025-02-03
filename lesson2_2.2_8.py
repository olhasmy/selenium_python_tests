from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan.petrov@example.com")

    file_name = "test_file.txt"
    file_path = os.path.abspath(file_name)
    with open(file_path, "w") as file:
        file.write("Test file content")

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(10)

finally:
    browser.quit()
    if os.path.exists(file_path):
        os.remove(file_path)
