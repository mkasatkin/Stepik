import unittest
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)



class TestSys(unittest.TestCase):

    def test_link2(self):
        element_registration = browser.find_element_by_css_selector('h1').text
        self.assertEqual(element_registration, 'Registration', "page_open_error")
        name = browser.find_element_by_css_selector('.first_block>.first_class>.first')
        name.send_keys('Моточек')
        self.assertEqual(name.get_attribute('placeholder'), 'Input your name', "name_past_error")
        lastname = browser.find_element_by_css_selector('.first_block>.second_class>.second')
        lastname.send_keys('Ниточек')
        self.assertEqual(lastname.get_attribute('placeholder'), 'Input your last name', "last_name_past_error")
        mail = browser.find_element_by_css_selector('.first_block>.third_class>.third')
        mail.send_keys('itisoktobe@grey.too')
        self.assertEqual(mail.get_attribute('placeholder'), 'Input your email', "mail_past_error")
        button = browser.find_element_by_tag_name("button")
        button.click()
        congratulation = browser.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!', "button_click_error")

class TestSystem(unittest.TestCase):
    def test_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        element_registration = browser.find_element_by_css_selector('h1').text
        self.assertEqual(element_registration, 'Registration', "page_open_error")
        name = browser.find_element_by_css_selector('.first_block>.first_class>.first')
        name.send_keys('Моточек')
        self.assertEqual(name.get_attribute('placeholder'), 'Input your first name',  "name_past_error")
        lastname = browser.find_element_by_css_selector('.first_block>.second_class>.second')
        lastname.send_keys('Ниточек')
        self.assertEqual(lastname.get_attribute('placeholder'), 'Input your last name', "last_name_past_error")
        mail = browser.find_element_by_css_selector('.first_block>.third_class>.third')
        mail.send_keys('itisoktobe@grey.too')
        self.assertEqual(mail.get_attribute('placeholder'), 'Input your email', "mail_past_error")
        button = browser.find_element_by_tag_name("button")
        button.click()
        congratulation = browser.find_element_by_css_selector("h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!', "button_click_error")



if __name__ == "__main__":
    unittest.main()