def sort1(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return sort1(left) + middle + sort1(right)
dta= [10, 7, 8, 9, 1, 5]
a=sort1(dta)
print(a)