

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def driver_setup(request):
    browser=request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
         print("launching chrome firefox")
         driver = webdriver.Firefox()
    elif browser == "Edge":
         print("launching chrome edge")
         driver = webdriver.Edge()
    elif browser == "headless":
        print("launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    else:
        driver= webdriver.Chrome()

    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    print("\nBrowser closed")
    driver.quit()