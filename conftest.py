from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import yaml
import pytest

#config.yaml fixture
@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)
    
#driver fixture
@pytest.fixture(scope="function")
def driver(config):
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore_certificate_errors")
    # chrome_options.add_argument("--incognito") 
    driver=webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(5)
    driver.get(config["base_url"])
    yield driver
    driver.quit()

#wait fixture
@pytest.fixture
def wait():
    return WebDriverWait(driver,10)

