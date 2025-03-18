# def is_prime(num):
#
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
#
#
# for i in range(1,10):
#     if is_prime(i):
#         print(f"{i} is prime")
#     else:
#         print(f"{i} is not prime")

n=7

for i in range(n,n-1):
    print(i)
    if n%i==0:
        print(f"this is prime {i}")
    else :
        print(f"this is not prime{i}")



