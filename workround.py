# num_range=153
# num_range1 = len(str(num_range))
# amg_syrong=0
#
# while num_range> 0:
#     num = num_range % 10
#
#     amg_syrong =amg_syrong+ num ** num_range1
#
#     num_range //= 10
# print(amg_syrong)



def fibnoncci_series(num,fib):
# for i in range(num):

    for i in range(0,num):
        next1=fib[-2] + fib[-1]
        if next1>num:
            break
        fib.append(next1)
        # num = num - 1
        a=" ".join(map(str,fib))
    return a
fib = [0, 1]
obj=fibnoncci_series(15,fib)

# print(obj)




x=567
a=x%10
print(a)

num=x//10
print(num)

b=num%10
print(b)

c=num//10
print(c)

# Exercise 15: Write all content of a given file into a new file by skipping line number 5

list1=[]
with open(r"D:\New_folder\new_text_file","+r") as file:
    file_lins=file.readlines()
    for i in enumerate(file_lins):
        if i[0]==5:
            continue
        list1.append(i[1])
        print(list1)
    # for i in list1:
        # print(i)
    # print(a)
    with open(r"D:\New_folder\new_write","+w") as files:
        files_new=files.writelines(list1)



















