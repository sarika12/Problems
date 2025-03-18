a=[1, 2, 4, 5, 6]
count=1
for i in range(0,len(a)):
    # for j in range(i+1-1):
    str(a[i+1-1]).count(str(a[i]))
    print(a)
    # else:
    #     print(a[j])

aa1=[1, 2, 4, 5, 6]
length=len(aa1)+1
# print(length)
total=length*(length+1)//2
print(total)
print(total-sum(aa1))