var_dictionary = {'All': [1, 2, 3], 'is': [1, 4], 'well': [4, 2]}
dict1={}

for k,v in var_dictionary.items():
    if isinstance(v,list):
        for v1 in v:
            if v1 in dict1:
                dict1[v1].append(k)

            else:
                dict1[v1]=[k]
# print(dict1)


var_dictionary1 = {'All': [1, 2, 3], 'is': [1, 4], 'well': [4, 2]}

list1=[]
dict11={}

for key,values in var_dictionary1.items():
# print(list111)

    for values1 in values :
        if values1 in dict11:
            dict11[values1].append(key)
        else:
            dict11[values1]=[key]
print(dict11)


