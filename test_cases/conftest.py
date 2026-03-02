import pytest
from pytest_metadata.plugin import metadata_key

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome",help="specify browser: chrome or firefox or edge")



@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    yield driver
    driver.quit()


# def pytest_configure(config):
#     config.stash[metadata_key] ['Project Name'] = "NopCommerce"
#     config.stash[metadata_key] ['Test Module Name'] = "Admin Login Tests"
#     config.stash[metadata_key] ['Tester Name'] = "Prashant"


