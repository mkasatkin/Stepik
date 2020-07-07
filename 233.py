import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    xel = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = xel.text
    y = calc(x)
    q = browser.find_element(By.XPATH, "//input")
    q.send_keys(str(y))
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()