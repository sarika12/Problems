#Reverse the vowels in each word of a given string.
str1 = "sammme hello dame a"
Output= "semmma holle dema a"

def reverse_vowels(word):
    vowles="aeiouAEIOU"
    word_list=list(word)
    # print(word_list)

    i,j =0,len(word)-1
    print(len(word)-1)

    # while i < j:
    #     pass




str11 = "sammme hello dame a"
words = str11.split()
word1 = [reverse_vowels(words) for word in words]
output = reverse_vowels(words)
print(output)



