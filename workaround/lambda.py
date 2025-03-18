a=list(filter(lambda x:x%2==0 ,(i for i in range(51))))
print(a)


ini_dict = {'geeks': {'Geeks': {'for': 7}},
           'for': {'geeks': {'Geeks': 3}},
           'Geeks': {'for': {'for': 1, 'geeks': 4}}}

def flaten_dict(in_dict,out_dict=None,prefix=None,seperater="_"):
    # out_dict={}
    if out_dict is None:
        out_dict={}
    for k,v in in_dict.items():
        k=f'{prefix}{seperater}{k}' if prefix else k
        if isinstance(v,dict):
            flaten_dict(in_dict=v,out_dict=out_dict,prefix=k)
            continue
        out_dict[k]=v
    return out_dict

print(flaten_dict(ini_dict))








