MARKERS = {
    b"i": int,
    b"l": list,
    b"d": dict,
}


def get_datatype(byte: bytes):
    return MARKERS[byte]
