str1 = "P@#yn26at^&i5ve"
dig=0
lett=0
sp=0
for i in range(len(str1)):
    if str1[i].isdigit():
        dig=dig+1
    elif str1[i].isalpha():
        lett=lett+1
    else:
        sp=sp+1
print(dig)
print(lett)
print(sp)
