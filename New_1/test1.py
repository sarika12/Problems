from collections import Counter

# Write a program to count occurrences of all characters with a string Apple

# from collections import Counter
#
string="Apple"
#
str1=" ".join(string).split()
a=Counter(str1)
print(a)

# find the length of the longest substring without repeating characters
import random
string="abcabcbb"
# a=" ".join(string).split()
# print(a)
# list1=[]
# for i in range(len(string)):
#     for j in range(len(string)-i-1):
#         if string[i]!=string[j] and string[i]>string[j]:
#             list1.append(string[j])
# print(list1)

char_index={}
max_lenth=0
left=0
for right ,char in enumerate(string):
    if char in char_index.values()  and char_index[right]>=left:
        left=char_index[char]+1
    char_index[char]=right
    print(char_index)


# from itertools import permutations
#
# per=permutations(string)
# for a in per:
#     print(''.join(a))
#



# temp=" "
# for str1 in range(len(string)):
#     if






