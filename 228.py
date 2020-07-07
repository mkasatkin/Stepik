import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.XPATH, "//input[@name='firstname']")
    x.send_keys("Зубенко")
    x = browser.find_element(By.XPATH, "//input[@name='lastname']")
    x.send_keys("МихаилПетрович")
    x = browser.find_element(By.XPATH, "//input[@name='email']")
    x.send_keys("qweasd@qwdsa.qwe")
    element = browser.find_element(By.XPATH, "// input[ @ id = 'file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()