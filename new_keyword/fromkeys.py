a = [1, 2, 3, 3, 4, 4, 5, 5]
print(dict.fromkeys(a))
List_salary= [1000,20000,5000,50000,30,2000]
def second_highest():
    List_salary.sort()
    print(List_salary[-2])

a=second_highest()

even_num=[]
odd_num=[]
a1=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
for a in range(len(a1)):
    if a%2==0:
        even_num.append(a1[a])
    else:
        odd_num.append(a1[a])
print(even_num)
print(odd_num)
even_num.extend(odd_num)
print(even_num)

sort_list=[130, 200,20000,300,400]

for sort1 in range(len(sort_list)):
    for sort2 in range(0,len(sort_list)-sort1-1):
        if sort_list[sort2]>sort_list[sort2+1]:
            sort_list[sort2],sort_list[sort2+1]=sort_list[sort2+1],sort_list[sort2]

print(sort_list)

string1="this is sarika she is good"
string2=string1.split()
print(string2)
count1=1
dict1={}
for i in string2:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)

Input="aaabbbacfwww"



current_char=Input[0]
count=1
output=""

for i in range(1,len(Input)):
    if Input[i]==current_char:
        count+=1
    else:
        a=(str(count) if count>1 else "")
        output += current_char +a
        current_char=Input[i]
        print(current_char)
        count=1
output+=current_char+(str(count))
print(output)
s=input("Enter the some string:")

i=len(s)-1
terget=""
while i>0:
    terget=terget+s[i]
    i=i-1
print(terget)




