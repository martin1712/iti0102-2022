

"""EX02 - Math."""

def add(x: int, y: int):
    """Add function."""
    x + y
    return x + y


def sub(x: int, y: int):
    """Sub finction."""
    x - y
    return x - y


def multiply(x: int, y: int):
    """Multiply function."""
    x * y
    return x * y


def div(x: int, y: int):
    """Div function."""
    x / y
    return x / y


def modulus(x: int, y: int):
    """Modulus function."""
    x % y
    return x % y


def floor_div(x: int, y: int):
    """Floor div function."""
    x // y
    return x // y


def exponent(x: int, y: int):
    """Exponent function."""
    x ** y
    return x ** y


def first_greater_or_equal(x: int, y: int):
    """First_greater_or_equal function."""
    x >= y
    return x >= y


def second_less_or_equal(x: int, y: int):
    """Second_less_or_equal function."""
    y <= x
    return y <= x


def x_is_y(x: int, y: int):
    """x_is_y function."""
    x == y
    return x == y


def x_is_not_y(x: int, y: int):
    """x_is_not_y function."""
    x != y
    return x != y


def surface(x: int, y: int):
    """Surface function."""
    x * y
    return x * y


def volume(a: int, b: int, c: int):
    """Volume function."""
    a * b * c
    return a * b * c


def clock(päevad: int, tunnid: int, minutid: int, sekundid: int):
    """Clock function."""
    a = päevad * 1440
    b = tunnid * 60
    c = minutid
    d = sekundid / 60
    return a + b + c + d


def calculate(a: int, b: int, c: int):
    """Calculate function."""
    if a == 0:
        return b + c
    if a == 1:
        return b - c
    if a == 2:
        return b * c
    if a == 3:
        return b / c


def if_else(a: int, b: int, c: int, d: int):
    """If_else function."""
    first = a * b
    second = c / d
    if first > second:
        return first
    if second > first:
        return second
    if first == second:
        return 0
