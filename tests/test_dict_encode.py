import pytest

from src.dict_encode import dict_encode


def test_dict_encode_basic():
    """Проверка базового корректного словаря."""
    data = b"3:foo3:bar4:name4:alex"
    expected = {"foo": b"bar", "name": b"alex"}
    assert dict_encode(data) == expected


def test_dict_encode_empty():
    """Проверка пустого входа."""
    assert dict_encode(b"") == {}


def test_dict_encode_long_values():
    """Проверка работы с длинными строками и спецсимволами."""
    data = b"4:text12:hello world!4:type4:test"
    result = dict_encode(data)
    assert result["text"] == b"hello world!"
    assert len(result) == 2


def test_dict_encode_numeric_strings():
    """Проверка, когда ключи или значения выглядят как числа."""
    data = b"1:11:21:31:4"
    assert dict_encode(data) == {"1": b"2", "3": b"4"}


def test_dict_encode_invalid_format():
    """Проверка поведения при некорректном формате (ожидаем ошибку)."""
    invalid_data = b"not_a_bencode_format"
    with pytest.raises(ValueError):
        dict_encode(invalid_data)


@pytest.mark.parametrize(
    "input_bytes, expected_dict",
    [
        (b"2:id1:1", {"id": b"1"}),
        (b"3:key10:0123456789", {"key": b"0123456789"}),
    ],
)
def test_dict_encode_parameterized(input_bytes, expected_dict):
    """Параметризованный тест для разных входных данных."""
    assert dict_encode(input_bytes) == expected_dict
