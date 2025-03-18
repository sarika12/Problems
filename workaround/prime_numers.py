upar_range=2
lowe_range=15

for i in range(2,15):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                # print("numer is not prime",i)
                break
        else:
            print("numer is prime",i)