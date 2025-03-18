from new_8.calculater import Calculator
import pytest


@pytest.fixture
def cal():
    return Calculator()
@pytest.fixture()
def my_fixture():
    return [1, 2, 3]