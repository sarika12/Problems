a="AABBBCCCCaaaaa"
list1=[]
a1=sorted(set(a))
# print(a1)
for i in a1:
    b=a.count(i)
    list1.append(i+str(b))
print("".join(list1))