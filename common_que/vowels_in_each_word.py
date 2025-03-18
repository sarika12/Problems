#Reverse the vowels in each word of a given string.
str1 = "sammme hello dame a"
Output= "semmma holle dema a"
vowels=["a","e","i","o","u"]
str2=str1.split()
for word1 in str2:
    if len((word1))>1:
        # word=[str2[word1]]
        # print(word)
        a=word1[-1:]
        b=word1[1:2]
        c=word1[0]+a+word1[2:len(word1)-1]+b
        # (str2[word][1]),(str2[word][-1])=str2[word][-1],str2[word][1]
        print(c)

    else:
        swp=word1
        print("single length ->",word1)
    # print(c)












