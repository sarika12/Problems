input="a4b3c2"
# output="aaaabbbcc"
output=""
for x in input:
    if x.isalpha():
        output=output+x
        prv=x
        print(x)
    else:
        output=output+prv*(int(x)-1)
print(output)


