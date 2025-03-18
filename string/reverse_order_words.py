# s=input("enter some word: ")

s="this is sarika"
# n=len(s)
list1=s.split()
n=len(list1)-1
list2=[]
while n>=0:
    list2.append(list1[n])
    n=n-1
print(list2)