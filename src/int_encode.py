def int_encode(bytes: bytes) -> int:
    if bytes.startswith(b"-0"):
        raise ValueError("Starts with -0")

    return int(bytes)
