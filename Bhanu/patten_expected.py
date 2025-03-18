List_l1 = [1,2,3,4,5]
# expected_result = {"1":14, "2":13,"3":12,"4":11,"5":10}

dict1={}
for i in range(len(List_l1)-1,-1,-1):
    dict1[len(List_l1)-i]="1"+str(i)
print(dict1)

