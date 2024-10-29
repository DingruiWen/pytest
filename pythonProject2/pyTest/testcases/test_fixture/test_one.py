import pytest


@pytest.fixture(scope="class")
def func():
    print("previous step")

@pytest.mark.usefixtures("func")
class TestExample:
    def test_one(self):
        expect = 1
        actual = 1
        assert expect==actual

    def test_two(self):
        expect = 1
        actual = 1
        assert expect==actual

if __name__ == '__main__':
    pytest.main()
