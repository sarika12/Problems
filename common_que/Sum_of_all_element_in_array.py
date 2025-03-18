integer=input().split()
print(integer)

n=len(integer)
i=0
sum1=0
while n>i:
    sum1=int(integer[i])+sum1
    i+=1
print(sum1)
