# Rotate by 2

#Write a program to rotate an array to the right by a given number of steps. Example:
# Input: [1, 2, 3, 4, 5], Rotate by 2
# Output: [4, 5, 1, 2, 3]
a1=[1,2,3,4,5]
i=0
rot=3
while i<rot:
    a2=a1[0:len(a1)-1]
    print(a1)
    a2.insert(0,a1[-1])

    a1=a2
    i+=1
print(a2)