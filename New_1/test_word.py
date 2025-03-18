# Sample Input
# ------------
# 4
# bcdef
# abcdefg
# bcde
# bcdef
#
# Sample Output
# -------------
# 3
# 2 1 1
from collections import Counter
list_word=[]
to_check_len=[]
n=5
for _ in range(n):

    enter=str(input())
    list_word.append(enter)

word=Counter(list_word)
print(word)
for k,v in word.items():
    to_check_len.append(k)
    print(v,end=" ")
print(" ")
print(len(to_check_len))






