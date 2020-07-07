import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:

    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    xel = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = xel.text
    y = calc(x)
    q = browser.find_element(By.XPATH, "// input[ @ id = 'answer']")
    q.send_keys(str(y))
    browser.execute_script("window.scrollBy(0, 100);")
    option1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    option2.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:

    time.sleep(10)
    browser.quit()