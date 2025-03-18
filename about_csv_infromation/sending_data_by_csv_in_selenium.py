import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


with open("user.csv",mode="r") as file:
    reader1=csv.reader(file)
    header=next(reader1)
    optis = Options()
    driver = webdriver.Chrome(options=optis)
    driver.get("https://www.demoblaze.com/")
    for row in reader1:
        username=row[0]
        pasword=row[1]
        # print(username)
        # print(pasword)

        time.sleep(2)
        login_btn = driver.find_element(By.ID, "login2")
        login_btn.click()
        time.sleep(2)

        enter_username=driver.find_element(By.ID,"loginusername")
        enter_username.send_keys(username)
        time.sleep(2)
        enter_password=driver.find_element(By.ID,"loginpassword")
        enter_password.send_keys(pasword)
        time.sleep(2)
        login=driver.find_element(By.XPATH,"//button[text()='Log in']")
        login.click()
        logout=driver.find_element(By.ID,"logout2")
        logout.click()
driver.quit()