
def factoral(n):
    # fact=1
    if n<0:
        print("fact is not negitive")
    fact=1
    for i in range(1,n+1):
        fact=fact*i




    return fact


a=factoral(6)
print(a)