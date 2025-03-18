s="nndhjgjk"
sub="a"
flag=False
pos=-1
n=len(s)

while True:
    pos=s.find(sub,pos+1,n)
    # print(pos)
    if pos==-1:
        break
    print("found at pos",pos)
    flag=True
if flag==False:
    print("not found")

