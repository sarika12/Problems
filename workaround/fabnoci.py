fab=[0,1]
n=5
list1=[]
for i in range(n):
    fab.append(fab[-1]+fab[-2])
print(fab)
