# str1="sarika"
#
# print(str1[-1::-2])
input1=input()
list1=[]

with open(r"D:\New_folder\new_2\Request-ID-list.txt","+r") as files:
    file=files.readlines()
    for f in file:
        if input1 not in f :
            print("invald")
        try:
            if input1 in f:
                list1.append(input1)
                print(list1[0])
        except Exception as a:
            print(a)



input2=input()
with open(r"D:\New_folder\new_2\Request-ID-list.txt","+r") as files:
    file=files.readlines()
    print(file)
    if input2 in file :
        print(input2)
    else:
        print("invalid")
