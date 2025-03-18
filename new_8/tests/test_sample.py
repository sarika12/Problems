import pytest

from new_8 import reverse_text_string



def test_sum(my_fixture):
    assert sum(my_fixture) == 6
def test_reveres_text_non_string():
    with pytest.raises(ValueError):
        reverse_text_string.reversed_text("1345")