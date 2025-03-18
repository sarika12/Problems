import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# header={"content":"text/plain",
#     "application":"xyz"
# }
#
# response=requests.get(url="/13",headers=header,json="")
#
# payload ={id:"12",
#     "name":"sarika"
# }
#
#
# response2=requests.post(url="/14",headers=header,json =payload)
# print(response2.status_code)
#



def broswer():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.in")

    driver.quit()


class Televison:

    def __init__(self, brand):
        self._brand = brand

    def trun_on(self):
        print("trun on the tv")

    def _brand_name(self):
        print(self._brand)


class sony(Televison):
    pass


cls1 = Televison("abc")
cls1._brand_name()
cls1.trun_on()
clss2 = sony("xyz")

# Online Python compiler (interpreter) to run Python online.
from collections import Counter

str1 = "sarika shrivastava"
str2 = Counter(str1)
print(str2)

list1 = []
list12=[]
max_freq = max(str2.values())
for k, v in str2.items():
    if v==max_freq:
        print(k)


# find duplicate word in give string

str1="sarika"
dict1={}
for char in str1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1

for k,v in dict1.items():
    if v>1:
        print(k)

a1=list(range(0,5))
print(a1)

a=[1,0,3,0,1,0,1,0]
a1=[]
a2=[]
for i in range(len(a)):
    # for j in range(i+1):
    if '0' in str(a[i]):
        a1.append(a[i])
    else:
        a2.append(a[i])
# print(a1)
# print(a2)

a2.extend(a1)
print(a2)











