a="{[()]}"

b="({[)}]"


stack=[]

for top in a:
    if top=="{" and top=="}":
        print("True")

    elif top=="[" and top=="]":
        print("True")
    elif top=="(" and top==")":
        print("True")

a=[]
print(not a)

