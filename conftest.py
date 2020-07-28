import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver=webdriver.Chrome()
    elif browser_name == "firefox":
        driver=webdriver.Firefox()
    elif browser_name == "IE":
        driver=webdriver.IE()    
        
    driver.implicitly_wait(10)
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
