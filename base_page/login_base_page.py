
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class login_base_page:

    usernamexpath = "//input[@name='username']"
    passwordxpath = "//input[@name='password']"
    login_buttonxpath = "//button[@type='submit']"
    profilexpath = "//p[@class='oxd-userdropdown-name']"
    logout_button = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_username(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.usernamexpath)))

    def enter_password(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.passwordxpath)))

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login_buttonxpath))).click()

    def click_profile(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.profilexpath))).click()

    def click_logout(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.logout_button))).click()