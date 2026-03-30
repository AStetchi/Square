def int_encode(data: bytes) -> int:
    """
    This module provides a function to encode bytes into an integer.
    It checks for a specific case where the byte string starts with "-0"
    and raises a ValueError if that is the case. Otherwise, it converts
    the byte string to an integer using the built-in int() function.
    """
    if data.startswith(b"-0"):
        raise ValueError("Starts with -0")

    return int(data)
