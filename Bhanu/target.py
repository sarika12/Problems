
# Input = [2,7,11,15], target = 9, find the element indices whose sum is equal to target and
# output=[0,1]
Input = [2,7,11,15]
target = 9


for i in range(len(Input)):
    for j in range(0,i+1-1):
        if target==Input[i]+Input[j]:
            a=[i,j]
print(a)
