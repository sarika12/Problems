# class Calculater:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def addition(self):
#         c=self.a+self.b
#         print(c)
#
# obj=Calculater(3,2)
# obj.addition()


# array = [2, 7, 12, "my_name", "malayalam"]
# for arr in array:
#     if type(arr)==int:
#         print(f"not valid {arr}")
#     elif arr==arr[::-1]:
#         print(f"string is palidrom {arr}")


# data = {
#     "name": "John",
#     "age": 30,
#     "address": {
#         "street": "28, Main street",
#         "town": "Banglore",
#         "state": "KA"
#     },
#     "response": {
#         "numFound": 3,
#         "start": 0,
#         "docs": [{"language": "English", "count": 4, "percent": 70},
#                  {"language": "Spanish", "count": 3, "percent": 70},
#                  {"language": "French", "count": 2, "percent": 70}]
#     }
#
# }
# data1=data["response"]
# a=data1['docs'][1]
# print(a['count'])




# How do you validate a password using Python for below conditions,
# a. Length of password : Min-8 to Max-14
# b. one special char
# c. one lower char
# d. one upper char
# e. one digit

pass1="Aa1234567@12"
def valid():
    if len(pass1)>=8 and len(pass1)<=14:
        for p1 in range(len(pass1)):
            if pass1[p1].isdigit() and pass1.islower() and pass1.isupper() and pass1.isupper():
                print("valid")
            else:
                print("spcial")
    return True

            # print(f"digit is present{pass1[p1]}")
# pass1.islower():
#             print(f"lower char are present{pass1[p1]}")
#         elif pass1.isupper():
#             print(f"lower char are present{pass1[p1]}")
#         else:
#             print(f"special char {pass1[p1]}")



















