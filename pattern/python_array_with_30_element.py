# arr = [i for i in range(30)]
# x`print(arr)


list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30]
out=[]
for i in range(0,len(list1),5):
    if (i//5)%2==1:
        out.extend(list1[i:i+5][::-1])
    else:

        out.extend(list1[i:i+5])

print(out)
for i in range(10):
    print((i//5)%2==1)


    # if i%5==0:

