import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

@pytest.fixture()
def browser():
    option=Options()
    driver=webdriver.Chrome(options=option)
    driver.maximize_window()
    yield driver

def test_google_serch(browser):
    browser.get("https://www.google.com")
    print(browser.title)
    assert "Google" in browser.title