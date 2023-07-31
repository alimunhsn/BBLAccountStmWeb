import pytest
from selenium import webdriver

from src.Configure.readPropertices import conf


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.get(conf.getApplicationURl())
    return driver
