import random
from random import randint

def random_num():

    number='.'.join(str(randint(0,255)) for _ in range(4))
    return number
# lis_com=[ ".".join(str(randint(0,255)) for _ in range(4))]
# print(lis_com)
for i in  range(5):
    print(random_num())
    # print(lis_com)

def random1():
    num1=".".join(str(randint(0,255)) for i in range(4))
    return num1

# list1=""
for i in range(4):
    print(random1())