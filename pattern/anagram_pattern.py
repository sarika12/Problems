a=["bbac","abcb","acbb"]

from collections import Counter
def slove(s1,s2,s3):


    a=Counter(s1)
    b=Counter(s2)
    c=Counter(s3)
    for k,v in a.items():
        if a[k]==b[k]==c[k]:
            return "YES"
        else:
            return "NO"


s1=input()
s2=input()
s3=input()
s=slove(s1,s2,s3)
print(s)