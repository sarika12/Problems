def binary_search(a,trget):
    low=0
    high=len(a)-1

    while low<=high:
        mid = (low + high) // 2
        if a[mid]==trget:
            return mid
        elif a[mid]<trget:
            low=mid+1
        else:
            high=mid-1
    return -1

a=[1,2,3,4,5,6,7,8,9]
trget=6
b=binary_search(a,trget)
print(b)