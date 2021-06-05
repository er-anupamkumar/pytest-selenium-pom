from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON= (By.ID,"btnLogin")
    ERROR_FIELD= (By.ID,"spanMessage")
    CREDENTIALS_FEILD=(By.XPATH,"//*[@id=\"content\"]/div[2]/span")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self,title):
        return self.get_title(self,title)

    def do_login(self,username,password):
         self.do_send_keys(self.USERNAME,username)
         self.do_send_keys(self.PASSWORD,password)
         self.do_click(self.LOGIN_BUTTON)

    def get_ErrorMessage(self):
        return self.get_element_text(self.ERROR_FIELD)

    def get_ProvidedUserName(self):
        credentialsText= self.get_element_text(self.CREDENTIALS_FEILD)
        username = credentialsText.split("|")[0].split(":")[1].strip();
        return username

    def get_ProvidedPassword(self):
        credentialsText= self.get_element_text(self.CREDENTIALS_FEILD)
        password = credentialsText.split("|")[1].split(":")[1].replace(")", "").strip();
        return password

