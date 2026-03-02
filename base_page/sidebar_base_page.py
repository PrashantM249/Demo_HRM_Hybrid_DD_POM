import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class sidebar_base_page:
    adminoptionxpath = "//span[text()='Admin']"
    add_admin_button = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    user_role = "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]"
    ess_role = "//div[text()='ESS']"
    employee_name = "//input[@placeholder='Type for hints...']"
    status = "(//div[text()='-- Select --'])[2]"
    username = "(//input[@class='oxd-input oxd-input--active'])[2]"
    password = "//label[text()='Password']/following::input[@type='password'][1]"
    confirm_password = "//label[text()='Confirm Password']/following::input[@type='password'][1]"
    save_button = "//button[@type='submit']"
    admin_dashboard_username = "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click_admin(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,self.adminoptionxpath))).click()

    def click_add_admin(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,self.add_admin_button))).click()


    def user_admin_role(self, role_name):
        # Click dropdown
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
            )
        ).click()

        # Select option dynamically
        option_xpath = f"//div[@role='option']//span[text()='{role_name}']"

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

    def employee_admin_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,self.employee_name)))

    def user_status_admin(self,status_value):
        # Click Status dropdown
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
            )
        ).click()

        # Dynamic option selection
        option_xpath = f"//div[@role='option']//span[text()='{status_value}']"

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()


    def username_of_admin(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def enter_password(self, value):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.password))
        ).send_keys(value)

    def enter_confirm_password(self,value):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.confirm_password))).send_keys(value)

    def save_admin_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button))).click()

    def enter_admin_dashboard_username(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.username)))





