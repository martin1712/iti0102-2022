

"""Maths exercise."""


def average(a: int, b: int, c: int, d: int) -> float:
    """Average function."""
    a_1 = a * 1
    b_1 = b * 2
    c_1 = c * 3
    d_1 = d * 4
    return (a_1 + b_1 + c_1 + d_1) / 4


def school_pressure(ects: int, weeks: int) -> float:
    """School_pressure function."""
    a = ects * 26
    b = weeks * 168
    if a > b:
        return -1
    if weeks > 0:
        return a / weeks
    if weeks == 0:
        return -1


def add_fractions(a: int, b: int, c: int, d: int) -> str:
    """Add_fractions function."""
    x = a * d + b * c
    y = b * d
    if y == 0:
        return "-1"
    else:
        return (f"{x} / {y}")
