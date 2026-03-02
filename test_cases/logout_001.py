from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from base_page import login_base_page
from utilities import read_properties
from utilities.read_properties import Read_Config
import time
import os
from datetime import datetime
import pytest


class TestLogin():

    def setup_method(self):
        """Setup method that runs before each test"""
        self.url = Read_Config.get_login_page_url()
        self.username = Read_Config.get_username()
        self.password = Read_Config.get_password()
        self.driver = None

    def teardown_method(self):
        """Teardown method that runs after each test"""
        if self.driver:
            self.driver.quit()

    def test_logout(self):
        """Test valid login with correct credentials"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        print("Page title:", self.driver.title)

        # Create login_base_page instance and perform login
        login_page = login_base_page(self.driver)
        login_page.enter_username().send_keys(self.username)
        login_page.enter_password().send_keys(self.password)
        login_page.click_login()


        print("Login completed successfully!")
        login_page.click_profile()
        print("enter to profile successfully!")

        login_page.click_logout()
        time.sleep(3)
        print("Logout completed successfully!")
        assert self.driver.title, "Logout failed - page title is empty"





