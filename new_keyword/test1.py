lisst1=[1,0,1,2,0,3,0,0]
out=[1,2,2,3,0,0,0,0]

for li in range(len(lisst1)):
    for l2 in range(len(lisst1)-1-li):
        if lisst1[l2]>lisst1[l2+1]:
            lisst1[l2],lisst1[l2+1]=lisst1[l2+1],lisst1[l2]
print(lisst1[::-1])

str1="1/n121/n12321/n121/n1"
# 1
# 121
# 12321
# 121
# 1

n=5

for i in range(1,n+1):
    # for j in range(1,i+1):
    #     print(j, end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print("")
    # for k in range(1,n):
    #     for l in range(-1,-n):
    #         print(l,end=" ")
    print("")


print(list(range(n-1,0,-1)))
print(list(range(1,4)))


s=input("enter some string")
output=""
prv=0
for x in s:
    if x.isdigit():
        output=output+x
        prv=x
        # print(x)
        output=output+chr(ord(prv))+int(x)
        print(output)

a=ord("a")
print(a)