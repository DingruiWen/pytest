import pytest

def setup_function():
    print("set up")

def teardown_function():
    print("tear down")

def test_one():
    expect = 1
    actual = 1
    assert expect==actual

def test_two():
    expect = 1
    actual = 1
    assert expect==actual

if __name__ == '__main__':
    pytest.main()
