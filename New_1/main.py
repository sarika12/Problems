from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class LOGIN:
    def log_in_page(self):
        options=Options()
        driver=webdriver.Chrome(options=options)
        driver.get("www.paga.com")
        user_name=driver.find_element(By.XPATH,"").send_keys("sarika")
        user_pass=driver.find_element(By.ID,"").send_keys("xyz@123")
        submit_but=driver.find_element(By.ID,"").click()

obj=LOGIN()
obj.log_in_page()






