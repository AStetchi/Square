import pytest

from src.int_encode import int_encode


def test_positive_integer():
    assert int_encode(b"42") == 42
    assert int_encode(b"123456789") == 123456789


def test_zero():
    assert int_encode(b"0") == 0


def test_negative_integer():
    assert int_encode(b"-42") == -42
    assert int_encode(b"-1") == -1


def test_large_number():
    number = 10**18
    assert int_encode(str(number).encode()) == number


@pytest.mark.parametrize(
    "invalid_input",
    [
        b"abc",
        b"42a",
        b"1.5",
        b"",
        b"  ",
        b"++5",
        b"--5",
    ],
)
def test_invalid_input_raises_error(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        int_encode(invalid_input)


def test_leading_zeros_handling():
    assert int_encode(b"03") == 3


def test_negative_zero():
    assert int_encode(b"-0") == 0
