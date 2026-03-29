def int_encode(bytes: bytes) -> int:
    if bytes.startswith("-0"):
        raise ValueError("Starts with -0")

    bytes = bytes.copy()
    negative = bytes.startswith("-")
    num = 0

    if negative:
        bytes = bytes[1:]

    for place, digit in enumerate(bytes[::-1]):
        if not digit.isdigit():
            raise TypeError(f"{digit} is not a digit")

        num += int(digit) * (10**place)

    return num
