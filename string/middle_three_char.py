# str1 = "i"


def string1(str1):
    str2 = len(str1)
    if len(str1)>0:
        for i in  range(str2):
            length =str2//2
            print(length)
            if length:
                return str1[length-1:length+2]

        else:
            return "No string"
    else:
        return "String is empty"
str1 = ""

a=string1(str1)
print(a)



