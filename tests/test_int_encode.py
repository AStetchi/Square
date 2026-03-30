import pytest

from src.int_encode import int_encode


def test_int_encode_positive_single_digit():
    """Test encoding positive single digit integers."""
    assert int_encode(b"5") == 5
    assert int_encode(b"0") == 0
    assert int_encode(b"9") == 9


def test_int_encode_positive_multi_digit():
    """Test encoding positive multi-digit integers."""
    assert int_encode(b"42") == 42
    assert int_encode(b"12345") == 12345
    assert int_encode(b"999") == 999


def test_int_encode_negative_integers():
    """Test encoding negative integers."""
    assert int_encode(b"-1") == -1
    assert int_encode(b"-42") == -42
    assert int_encode(b"-12345") == -12345
    assert int_encode(b"-999") == -999


def test_int_encode_zero():
    """Test encoding zero."""
    assert int_encode(b"0") == 0


def test_int_encode_negative_zero_raises_error():
    """Test that -0 raises ValueError."""
    with pytest.raises(ValueError, match="Starts with -0"):
        int_encode(b"-0")


def test_int_encode_negative_zero_with_trailing_digits_raises_error():
    """Test that -0 followed by digits raises ValueError."""
    with pytest.raises(ValueError, match="Starts with -0"):
        int_encode(b"-01")
    with pytest.raises(ValueError, match="Starts with -0"):
        int_encode(b"-0123")
    with pytest.raises(ValueError, match="Starts with -0"):
        int_encode(b"-00")


def test_int_encode_leading_zeros():
    """Test that leading zeros are handled correctly (Python int() converts them)."""
    assert int_encode(b"007") == 7
    assert int_encode(b"00100") == 100
    assert int_encode(b"00") == 0


def test_int_encode_large_positive_integers():
    """Test encoding very large positive integers."""
    assert int_encode(b"999999999999999999999999999") == 999999999999999999999999999
    assert (
        int_encode(b"123456789012345678901234567890") == 123456789012345678901234567890
    )


def test_int_encode_large_negative_integers():
    """Test encoding very large negative integers."""
    assert int_encode(b"-999999999999999999999999999") == -999999999999999999999999999
    assert (
        int_encode(b"-123456789012345678901234567890")
        == -123456789012345678901234567890
    )
