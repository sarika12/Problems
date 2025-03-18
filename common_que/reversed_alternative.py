# #Reverse alternate words in a given string.
str1 = "selenium cypress playwright webdriverio"
Output= "selenium sserpyc playwright iorevirdbew"

str2=str1.split()
for st in range(len(str2)):
    if st%2!=0:
        print(str2[st][: : -1])
    else:
        print(str2[st])


count=1
def doThis():
    global count
    for i in (1,2,3):
        count+=1
doThis()
print(count)