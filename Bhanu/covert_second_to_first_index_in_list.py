list_ll2 = [1,2,3,4,5,6,7,9]
# exp_output = [2,1,4,3,6,5,8,7]
rs=[]
for i in range(0,len(list_ll2),2):
    # print(i)
    if i<len(list_ll2):
        rs.append(list_ll2[i+1])
        rs.append(list_ll2[i])
# print(rs)

rs1=[]
# for i in range(len(list_ll2)):
#     if i%2==0:
#         print(i)
#         rs1.append(list_ll2[i])
#         print(rs1)
#     else:
#         rs1.append(list_ll2[i+1])
print(rs1)
