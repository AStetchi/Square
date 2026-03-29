def int_encode(bytes: bytes) -> int:
    if bytes.startswith(b"-0"):
        raise ValueError("Starts with -0")

    negative = bytes.startswith(b"-")
    num = 0

    if negative:
        bytes = bytes[1:]

    for place, digit in enumerate(bytes[::-1]):
        digit -= 48
        if 0 < digit > 9:
            raise TypeError(f"{digit} is not a digit")

        num += digit * (10**place)

    return num if not negative else num * -1
