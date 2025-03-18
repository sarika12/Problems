# @pytest.mark.paramtized("name dept",[("sarika","QA"),("raja")])
from collections import Counter

# pyest -v xyz --html_report=""
# from collections import Counter

string1="working as a software from past 5 years"
string_app=[]
str1="".join(string1).split()
print(str1)
for i in range(len(str1)):
    str2=str1[i].title()
    string_app.append(str2)

print(" ".join(string_app))


class Bank:
    def __init__(self, salary, account_number):
        self.salary = salary
        self.__account_number = account_number

    def display(self):
        print(self.salary)
        print(self.__account_number)
class Empoyee(Bank):
    def display(self):
        print(self.salary)
        print(self.__account_number)




obj = Bank(10000, 3234146)
obj.display()

# print(str1)
# a=Counter(str1)
# print(a)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def open_url_flipkart():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.flipkart.com/")


















