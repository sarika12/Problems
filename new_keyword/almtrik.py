# 1) Given input prince123, find the sum of intgers , o/p should be 6
# 2) Given input prince, print 0 for e, 1 for c, 2 for n, 3 for i, 4 for r and so on
# 3) WAP to get all the broken links on a page using selenium
# 4) How do you handle dropdowns on a page
# 5) How can we get all the values from a dropdown on a page
# 6) Entered login and password and when clicking on submit, automation script fail how do you debug/handle it?

str1="prince1231134 sarika123"
a=0
for i in range(len(str1)):
    if str1[i].isdigit():

        a=a+int(str1[i])
# print(a)

for i in range(3):
    if i==2:
        break
else:
    print("..............")

def my_generater():
    yield 1
    yield 2
    yield 3


for value in my_generater():
    print(value)