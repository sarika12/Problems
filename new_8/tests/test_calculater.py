import pytest
# from new_8.calculater import Calculator
# from new_8 import Conftest

def test_addition(cal):
    assert cal.add(5,2)== 7
def test_subtract(cal):
    assert cal.subtract(5,2)==3
def test_division_zero(cal):
    with pytest.raises(ValueError):

        assert cal.divide(10,0)