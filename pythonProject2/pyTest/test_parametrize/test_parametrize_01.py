import pytest

@pytest.mark.parametrize("test_input,answer",[("3+5",8),("3*5",15),("2+1",3)])
def test_eval(test_input,answer):
    assert eval(test_input)==answer