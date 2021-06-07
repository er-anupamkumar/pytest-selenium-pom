from datetime import time

import pytest

from config.config import Configurations
from pages.Login import LoginPage
from tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_verify_login_unsuccessful(self):
        self.loginPage = LoginPage (self.driver)
        self.loginPage.do_login(Configurations.INVALID_USERNAME, Configurations.INVALID_PASSWORD)
        errorMessage = self.loginPage.get_ErrorMessage()
        assert errorMessage == "Invalid credentials: User not found"

    def test_verify_login_unsuccessful_when_password_empty(self):
        self.loginPage = LoginPage (self.driver)
        self.loginPage.do_login(Configurations.USER_NAME, "")
        errorMessage = self.loginPage.get_ErrorMessage()
        assert errorMessage == "Password cannot be empty"

    def test_verify_login_unsuccessful_when_username_empty(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("", Configurations.PASSWORD)
        errorMessage = self.loginPage.get_ErrorMessage()
        assert errorMessage == "Username cannot be empty"
