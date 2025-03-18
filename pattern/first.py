#4, 8,12,18,24,28 ,32,38
#4 4 6 6 4 4,6

a=4
b=6

# a+a=8
# out+a=12
# out+b=18
# out+b=24
# out+a=28


# current=a
output=[]

# for i in range(8):
#     output.append(current)
#     # print(output)
#
#     if i%2==0:
#         current += a
#     elif i%2!=0:
#         current+=b
# print(output)

# res=0
# i=0

# while i<6:
#     res=a+res
#
#     if i>2:
#         res=b+res
#         print(res)
#
#     i=i+1
#     print(res)

# count=1
current=4
output1=[]

Sequence=[4]
current1=4
step=[4,4,6,6]
for i in range(7):
    current1=current1+ step[i%4]
    Sequence.append(current1)
print(Sequence)

step1=[4,2]
for i in range(7):
    a=step1[i%2]
    print(a)

