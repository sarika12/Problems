number=153
num=len(str(number))
i=0
amstron_sum=0
while number>0:

    num1=number%10
    amstron_sum=amstron_sum+num1**num
    number//=10
print(amstron_sum)
