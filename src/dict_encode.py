from src.int_encode import int_encode


def dict_encode(data: bytes) -> dict:
    """Decodes a byte string into a dictionary."""

    output = {}

    idx = 0
    while idx < len(data):
        key_len_start = idx
        key_len_end = data.find(b":", idx)
        key_len = data[key_len_start:key_len_end]

        key_start = idx + len(key_len) + 1
        key_end = key_start + int_encode(key_len)
        idx = key_end

        value_len_start = idx
        value_len_end = data.find(b":", idx)
        value_len = data[value_len_start:value_len_end]

        value_start = idx + len(value_len) + 1
        value_end = value_start + int_encode(value_len)
        idx = value_end

        key = data[key_start:key_end]
        value = data[value_start:value_end]

        output[key.decode()] = value
    return output
