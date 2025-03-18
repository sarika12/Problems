from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
options=Options()
driver=webdriver.Chrome(options=options)
driver.get("http://www.google.co.in/")
driver.maximize_window()
# driver.minimize_window()
# driver.getsc
link=driver.find_elements(By.TAG_NAME,"a")

for li in link:
    get_link=li.get_attribute("href")
    if get_link is not None and get_link.startswith("https"):
        try:
            response=requests.get(url=get_link)
            if response.status_code>=400:
                print(f"broken link {get_link} and response code {response.status_code}")
            else:
                print(f"valid link {get_link} and response code {response.status_code}")
        except Exception as e :
            print(e)
driver.quit()
