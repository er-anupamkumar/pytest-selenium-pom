from selenium.webdriver.common.by import By

from config.config import Configurations
from pages.BasePage import BasePage

class HomePage(BasePage):

    WELCOME_LINK=(By.ID,"welcome")

    def __init__(self,driver):
        super().__init__(driver)

    def get_welcome_linkText(self):
        return self.get_element_text(self.WELCOME_LINK)