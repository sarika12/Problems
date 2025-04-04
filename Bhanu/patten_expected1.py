s = "kkccdddakk"
#output
# 2k2c3d1a2k
# a=0
prv=s[0]
str_len=len(s)
count=1
res=""
for index in range(1,str_len):
    if s[index]==prv:
        count+=1
    else:
        res=res+str(count)+prv
        prv=s[index]
        count=1

res=res+str(count)+prv
print(res)

# print(count)
#
