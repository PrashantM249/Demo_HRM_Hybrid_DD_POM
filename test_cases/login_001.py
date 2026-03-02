from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from base_page.login_base_page import login_base_page
from base_page.sidebar_base_page import Sidebar
from utilities import read_properties
from utilities.read_properties import Read_Config
from utilities import excel_utilities
import time
import os
from datetime import datetime
import pytest


class TestLogin:
    pathexcel = ".//test_data//Admin_login.xlsx"

    def setup_method(self):
        """Setup method that runs before each test"""
        self.url = Read_Config.get_login_page_url()
        self.username = Read_Config.get_username()
        self.password = Read_Config.get_password()
        self.invalidusername = Read_Config.get_admin_invalidusername()
        self.invalidpassword = Read_Config.get_admin_invalidpassword()
        self.driver = None


    def teardown_method(self):
        """Teardown method that runs after each test"""
        if self.driver:
            self.driver.quit()

    def test_login_valid(self):
        """Test valid login with correct credentials"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        print("Page title:", self.driver.title)

        self.username_excel = excel_utilities.read_excel(self.pathexcel ,"Sheet1" , 2 , 1 )
        self.userpass_excel = excel_utilities.read_excel(self.pathexcel, "Sheet1", 2, 2)
        # Create login_base_page instance and perform login
        login_page = login_base_page(self.driver)
        login_page.enter_username().send_keys(self.username_excel)
        login_page.enter_password().send_keys(self.userpass_excel)
        login_page.click_login()
        # profile = Sidebar(self.driver)
        # profile.click_admin()
        # Wait for login to complete


        print("Login completed successfully!")
        # assert self.driver.title, "Login failed - page title is empty"

    # def test_login_invalid(self):
    #     """Test login with invalid credentials"""
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     login_page = login_base_page(self.driver)
    #
    #     login_page.enter_username().send_keys(self.invalidusername)
    #     login_page.enter_password().send_keys(self.invalidpassword)
    #     login_page.click_login()
    #
    #     # Create screenshots directory if it doesn't exist
    #     screenshots_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
    #     os.makedirs(screenshots_dir, exist_ok=True)
    #
    #     # Generate timestamp for unique filename
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     screenshot_path = os.path.join(screenshots_dir, f"login_invalid_{timestamp}.png")
    #
    #     # Take screenshot
    #     self.driver.save_screenshot(screenshot_path)
    #     print(f"Screenshot saved at: {screenshot_path}")
    #
    #     time.sleep(3)
    #     print("Login with invalid credentials completed!")
    #     assert os.path.exists(screenshot_path), "Screenshot was not saved"



