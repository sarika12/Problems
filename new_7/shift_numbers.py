
#Shift all even numbers to left side of array and odd number to right side

def shift_number(array):
    right=len(array)-1
    left=0
    if left<right:
        for arr in range(len(array)):
            if array[arr]%2==0:
                left=left+1

            elif array[arr]%2!=0:
                right=right-1
            else:
                array[left],array[right]=array[right],array[left]
                right=right-1
                left=left+1
    return array




array1 = [12, 34, 45, 9, 8, 90, 3]
rst=shift_number(array1)
print(rst)





