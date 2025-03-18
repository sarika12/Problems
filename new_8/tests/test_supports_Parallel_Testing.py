import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def browser():
    options=Options()
    driver=webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("url",["https://www.google.com","https://www.bing.com","https://www.yahoo.com"])
def test_open_sites(browser,url):
    browser.get(url)
    assert browser.title