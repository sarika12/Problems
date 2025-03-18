import pytest

class Calculater:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addtion(self):
        c=a+b
        return c
    def muultifcation(self):
        if type(a)==str and type(b)==str:
            print("str is not valid")
        elif type(a)==list and type(b)==list:
            print("input not a list")
        else:
            c=a*b
            print(c)
    def subtraction(self):
        if type(a) == str and type(b) == str:
            print("str is not valid")
        elif type(a) == list and type(b) == list:
            print("input not a list")
        else:
            c = a * b
            print(c)
# a = "a"
# b = "a@"'/'" b"
a=3
b=5

cal=Calculater(a,b)
cal.addtion()
print("this is mutifcation")
cal.muultifcation()
print(".........")
cal.subtraction()
@pytest.fixture
def my_fixture():
    return cal
def test_addition(my_fixture):
    # cal = Calculater

    assert cal.addtion()==8







    # def divison1(self):
    #     if b>0:
    #         raise ZeroDivisionError
    #     else:
    #         c=


