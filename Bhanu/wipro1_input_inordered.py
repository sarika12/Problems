#Print the true or false by checking the input is ordered or not input is {[()]} 2nd input is ({[)}]

# input1="({[)}]"
# flg=True
# i1=len(input1)-1
# for i in range(len(input1)):
#     if input1[i]==input1[i-len(input1)]:
#         print(input1[i],input1[i1])
#         i1=i1-1
#
#         print(True)
#     else:
#         print(False)


s="{[()]}"
s1=len(s)-1
# print(s1)
trget=' '
# while s1>=0:
#     trget=trget+s[s1]
#     s1=s1-1
# print(trget)
# if trget==s:
#     print(True)
# else:
#     print(False)





# def is_order(s):
#     list1=[]
#     for char in s:
#         if char in "({[":
#             list1.append(char)
#         elif char==")":
#             if not list1 or list1.pop()!="(":
#                 return False
#         elif char=="}":
#             if not list1 or list1.pop!="{":
#                 return False
#         elif char==']':
#             if not list1 or list1.pop!="[":
#                 return False
#     return not list1

input1 = "{[()]}"
input2 = "({[)}]"
# print(is_order(input1))
# print(is_order(input2))
# def is_ordered(s):



stack=[]
order={"}":"{",")":"(","]":"["}
def order_is(s11):
    for char in s11:
        if char in order.values():
            stack.append(char)
        elif char in order.keys():
            if not stack or stack.pop()!= order[char]:
                return False
            else:
                continue
    return not stack
s11 = "{[()]}"
s22= "({[)}]"
print(order_is(s11))

























