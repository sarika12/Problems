s1="sarika shrivastava"
sub="a"
dict1={}
list1=[]
for s in s1:
    if s in dict1:
        dict1[s]+=1
    else:
        dict1[s]=1
print(dict1)

a=max(dict1.values())
for k,v in dict1.items():

    if v==a:
        print(k)




# flag=True
# pos=-1
# while True:
#     if pos==-1:
#
#         a=s1.find(sub,pos+1)
#
#         print("sub string index",a)
#         # flag = True
#         pos += 1
#         break
#     flag=True
#
# if flag==False:
#     print("no string")



