import pytest


class Calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    def subtract(self,a,b):
        return a-b
    def mutiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            raise ValueError("cannot divide by zero ")
        return a/b

@pytest.fixture
def cal():
    return Calculator()

def test_add(cal):
    assert cal.add(3,4)==7
