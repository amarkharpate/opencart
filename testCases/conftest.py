import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    return driver