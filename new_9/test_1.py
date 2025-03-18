import pytest


class Calculater:
    def sum1(self,a,b):
        return a+b


@pytest.fixture
def cal():

    a=Calculater()


def error():
    with pytest.raises(ValueError):
        raise("Value error ")
def test_cal(cal):
    b=cal.sum1(3,5)
    assert b==7
    assert error()




