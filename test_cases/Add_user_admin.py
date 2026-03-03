from logging import Logger

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from base_page.login_base_page import login_base_page
from base_page.sidebar_base_page import sidebar_base_page as Sidebar
from utilities import read_properties
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config
from utilities import excel_utilities
import time

import os
from datetime import datetime
import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:
    Add_user = ".//test_data//Add_User.xlsx"
    pathexcel = ".//test_data//Admin_login.xlsx"
    logger = Log_Maker.log_gen()

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

    def test_login_valid(self,setup):
        """Test valid login with correct credentials"""
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        print("Page title:", self.driver.title)

        self.username_excel = excel_utilities.read_excel(self.pathexcel ,"Sheet1" , 2 , 1 )
        self.userpass_excel = excel_utilities.read_excel(self.pathexcel, "Sheet1", 2, 2)
        self.employee_admin_name = excel_utilities.read_excel(self.Add_user, "Sheet1", 3, 1)
        self.employee_admin_username = excel_utilities.read_excel(self.Add_user, "Sheet1", 3, 2)
        self.employee_admin_password = excel_utilities.read_excel(self.Add_user, "Sheet1", 3, 3)
        self.employee_admin_confirm_password = excel_utilities.read_excel(self.Add_user, "Sheet1", 3, 4)

        self.logger.info("************login start**************")
        # Create login_base_page instance and perform login
        login_page = login_base_page(self.driver)
        login_page.enter_username().send_keys(self.username_excel)
        login_page.enter_password().send_keys(self.userpass_excel)
        login_page.click_login()
        self.logger.info("************click login**************")
        profile = Sidebar(self.driver)
        profile.click_admin()
        time.sleep(2)
        profile.click_add_admin()
        profile.user_admin_role("ESS")
        profile.employee_admin_name().send_keys(self.employee_admin_name)
        time.sleep(4)
        profile.user_status_admin("Enabled")
        profile.username_of_admin().send_keys(self.employee_admin_username)
        profile.enter_password(self.employee_admin_password)
        profile.enter_confirm_password(self.employee_admin_confirm_password)
        profile.save_admin_button()
        time.sleep(2)
        profile.enter_admin_dashboard_username().send_keys(self.employee_admin_username)




        # Wait for login to complete


        print("Login completed successfully!")
        # assert self.driver.title, "Login failed - page title is empty"