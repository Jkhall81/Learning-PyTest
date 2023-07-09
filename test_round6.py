import main
import pytest


def test_round6():
    assert main.round6(3.5) == 4
    assert main.round6(4.2) == 4
    assert main.round6(5.8) == 6


def test_add():
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0
    assert main.add(0, 0) == 0


def test_multiply():
    assert main.multiply(2, 3) == 6
    assert main.multiply(-1, 5) == -5
    assert main.multiply(4, 0) == 0


if __name__ == '__main__':
    pytest.main()
