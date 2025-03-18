"""Increment a Number Represented as an Array:
Consider an array like [1, 2, 9], which represents the number 129. When you add one, the result should be [1, 3, 0].
Similarly, [9, 9, 9] should become [1, 0, 0, 0].
"""
array = [1, 2, 9]

arry="".join(str(i) for i in array)
arr1=int(arry)+1
arr2=str(arr1)
for i in arr2:
    print(i)
