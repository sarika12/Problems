tuples = [(1, 3), (4, 2), (5, 1)]

for i in tuples:
    a=sorted(tuples,key=lambda x:x[1])
print(a)
