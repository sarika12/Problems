import pytest


def reversed_text(text):
    return text[::-1]

@pytest.fixture
def my_fixture():
    return [1,2,3]

def revserse_text_no_string(text):
    from pdb import set_trace
    set_trace()
    if isinstance(text, int):
        raise ValueError("expecting string ")
    return text[::-1]
# @pytest.mark.regression
def test_sum(my_fixture):
    assert sum(my_fixture)==6
# @pytest.mark.smoke
def test_reversed_string():
    assert reversed_text("sarika")== "akiras"
def test_reversed_text():
    assert reversed_text(str(12345))==str(54321)
# @pytest.mark.smoke1

def test_not_string_text():
    with pytest.raises(ValueError):
        assert revserse_text_no_string(123456)==654321

