import math

import pytest
def my_fixture():
    return [1,2,3]
def test_sum(my_fixture):
    assert sum(my_fixture)==6
def func(x):
    return x+5

def test_func():
    a=func(5)
    assert a==11

@pytest.mark.parametrize("input1,output",[(5.667,5),(10.99,10)])
def test_floor_check(input1,output):
    assert output==math.floor(input1)

@pytest.mark.parametrize("input1,output",[(2,4),(8,16),(5,10)])
def test_squar_root(input1,output):
    assert output==math.sqrt(input1)