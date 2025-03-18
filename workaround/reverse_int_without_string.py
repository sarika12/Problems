a=1234567
num=0
list1=[]
while a>0:

    b=a%10
    list1.append(b)
    a=a//10
    print(a)
print("".join(str(i) for i in list1))

