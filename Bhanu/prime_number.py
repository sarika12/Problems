

def prime_number(range_number):
    for numberm in range(range_number+1):
        if numberm>1:
            for i in range(2,numberm):

                if numberm%i==0:
                    break

            else:
                print(numberm)
range_number=int(input("enter the number ="))
a=prime_number(range_number)




