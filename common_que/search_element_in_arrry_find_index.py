a=[2,4,6,7,8]

enter=(input().split())
print(enter)
for i in enter:
    if int(i) in a:
        print(f"element   {i} index ",a.index(int(i)))
    else:
        print(f"element are not in list {i}")




