import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(2)
    return driver



driver = get_driver()
dropdown = Select(driver.find_element(By.ID,"carBrands"))

print("Dropdown options ", dropdown.first_selected_option.text)
time.sleep(2)

dropdown.select_by_value("saab")
print("Dropdown options ", dropdown.first_selected_option.text)

time.sleep(2)
dropdown.select_by_index(2)
print("Dropdown options ", dropdown.first_selected_option.text)

time.sleep(2)
dropdown.select_by_index(3)
print("Dropdown options ", dropdown.first_selected_option.text)

time.sleep(2)

driver.quit()