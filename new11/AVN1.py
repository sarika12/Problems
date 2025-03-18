# str1="sarika"
#
# dict1={}
#
# for i in str1:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
# print(dict1)

# str1="sarika is this is"
# str2=str1.split()
# dict2={}
# for i in str2:
#     if i in dict2:
#         dict2[i]+=1
#     else:
#         dict2[i]=1

# print(dict2)
# count=0
# for k,v in dict2.items():
#     count=len(k)+count
# print(count)
#
#
list1=[1,2,8,4,11,3]

# for ls in list1:
#     if ls%2==0:
#         print(f"num is {ls} even")
#     else:
#         print(f"num is odd {ls}")

for ls in range(len(list1)):
    for ls1 in range(0,ls+1-1):
        if list1[ls1]>list1[ls1+1]:
            list1[ls1],list1[ls1+1]=list1[ls1+1],list1[ls1]
# print(list1[0])


str1="sarika"
# print(str1[::-1])
s=len(str1)-1
t=""
i=0

while i<=s:
    t=t+str1[s]
    s = s - 1
print(t)
#a
# a=1
#ariak



































