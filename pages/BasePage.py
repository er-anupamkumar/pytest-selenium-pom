from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is parent of pages"""
"""Contains all generic methods and utils"""

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
       element= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
       return element.text

    def is_enabled(self, by_locator):
       element= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
       return bool(element)

    def get_title(self, title):
       element= WebDriverWait(self.driver, 10).until(EC.title_is(title))
       return self.driver.title
