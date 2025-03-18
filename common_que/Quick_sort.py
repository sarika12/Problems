
def Quick_sort(data):


    if len(data)<=1:
        return data
    pivot=data[-1]
    left=[x for x in data[:-1] if x<=pivot]
    # middel=[x for x in data if x==pivot]
    right=[x for x in data[:-1] if x>pivot]
    # print(left)
    # print(right)
    return Quick_sort(left)+[pivot] +Quick_sort(right)


data=[3,11,8,1,13,12,7]

a=Quick_sort(data)
print(a)
# print(data)