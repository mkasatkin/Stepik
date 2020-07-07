import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    xel = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = xel.text
    y = calc(x)
    q = browser.find_element(By.XPATH, "//input")
    q.send_keys(str(y))
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
