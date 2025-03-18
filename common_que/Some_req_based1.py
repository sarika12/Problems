a="a4b3c2"

# dict1={}
# b=a[0: :2]
# print(b)
# c=a[1: :2]
# print(c)

b = a[0::2]
print(b)
c = a[1::2]
print(c)
# c=int(c)
for i in range(len(b)):
    e=b[i]
    print(e*int(c[i]))

