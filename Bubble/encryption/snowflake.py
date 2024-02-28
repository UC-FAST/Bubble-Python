from time import time_ns


def snowflake() -> int:
    snowid = 0

    for i in list(bin(time_ns()))[-45:-2]:
        snowid |= int(i)
        snowid <<= 1

    for i in range(10):
        snowid |= 1
        snowid <<= 1

    for i in range(12):
        snowid |= 0
        snowid <<= 1

    snowid >>= 1
    return snowid

