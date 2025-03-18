

def string1(s1,s2):
    s11=len(s1)
    s11=s11//2
    fs=s1[0:s11]
    ls=s1[s11:]
    return fs+s2+ls


s1 = "Ault"
s2 = "Kelly"
a=string1(s1,s2)
print(a)

#AuKellylt