import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

# option=Options()
# option.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=option)
# driver.get("")
# webdriver.FirefoxOptions()

@pytest.mark.parametrize("browser",["Chrome","Edge"])
def test_parallel_execution(browser):
    if browser=="Chrome":
        options=Options()
        driver=webdriver.Chrome(options=options)
    # elif browser=="FireFox":
    #     driver=webdriver.Firefox()
    elif browser=="Edge":
        driver=webdriver.Edge()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
#Note : On terminal following command need to run 
#Folder Name>pytest -n 2
