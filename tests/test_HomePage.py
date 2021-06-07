from datetime import time

import pytest

from config.config import Configurations
from pages.Home import HomePage
from pages.Login import LoginPage
from tests.test_base import BaseTest
import logging


class Test_HomePage(BaseTest):

    def test_verify_login_successful_print_welcome_Name(self):
        log = logging.getLogger(__name__)
        self.loginPage = LoginPage (self.driver)
        self.loginPage.do_login(self.loginPage.get_ProvidedUserName(),self.loginPage.get_ProvidedPassword())
        self.homePage = HomePage(self.driver)
        welcomeMessage = self.homePage.get_welcome_linkText()
        log.info("Read Message:  "+welcomeMessage)
        name= welcomeMessage.split(" ")[1]
        log.info("Name of the user: "+name)
        assert "Welcome" in welcomeMessage
