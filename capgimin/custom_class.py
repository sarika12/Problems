from selenium import webdriver
class WebdriverFactory:
    def __init__(self,browser="chrome"):
        if browser.lower()=="chrome":
            self.driver=webdriver.Chrome()
        elif browser.lower()=="firebox":
            self.driver=webdriver.Firefox()

        else:
            raise  ValueError("unsuported browser")
    def get_driver(self):
        return self.driver
def test_open_website():
    factory=WebdriverFactory("chrome")
    driver=factory.get_driver()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
