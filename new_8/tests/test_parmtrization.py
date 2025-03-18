
import pytest
@pytest.mark.parametrize("inpout, output",[(1,11),(2,11),(3,22)])
def test_mutification_11(inpout,output):
    assert 11*inpout==output

