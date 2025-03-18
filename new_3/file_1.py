import logging
from datetime import datetime
import os

file=datetime.now().strftime("%Y%m%d%H:%M")
file_joint=f"log_{file}.txt"
a=os.getcwd()
# os.makedirs(a,exist_ok=False)

file1=os.path.join(a,file_joint)
print(file1)

with open(file1,"w") as f:
    f.write("this is log file")


a="sarika@gmail.com"

import random
list1=["sarika@123","adr@1234"]
print(random.choice(list1))

