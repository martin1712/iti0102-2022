

# Add function.


def add(x: int, y: int):
    x + y
    return x + y


# Sub finction.


def sub(x: int, y: int):
    x - y
    return x - y


# Multiply function.


def multiply(x: int, y: int):
    x * y
    return x * y


# Div function.


def div(x: int, y: int):
    x / y
    return x / y


# Modulus function.


def modulus(x: int, y: int):
    x % y
    return x % y


# Floor div function.


def floor_div(x: int, y: int):
    x // y
    return x // y


# Exponent function.


def exponent(x: int, y: int):
    x ** y
    return x ** y


# First_greater_or_equal function.


def first_greater_or_equal(x: int, y: int):
    x >= y
    return x >= y


# Second_less_or_equal function.


def second_less_or_equal(x: int, y: int):
    y <= x
    return y <= x


# x_is_y function.


def x_is_y(x: int, y: int):
    x == y
    return x == y


# x_is_not_y function.


def x_is_not_y(x: int, y: int):
    x != y
    return x != y


# Surface function.


def surface(x: int, y: int):
    x * y
    return x * y


# Volume function.


def volume(a: int, b: int, c: int):
    a * b * c
    return a * b * c


# Clock function.


def clock(päevad: int, tunnid: int, minutid: int, sekundid: int):
    a = päevad * 1440
    b = tunnid * 60
    c = minutid
    d = sekundid / 60
    return a + b + c + d


# Calculate function.


def calculate(a: int, b: int, c: int):
    if a == 0:
        return b + c
    if a == 1:
        return b - c
    if a == 2:
        return b * c
    if a == 3:
        return b / c


# If_else function.


def if_else(a: int, b: int, c: int, d: int):
    first = a * b
    second = c / d
    if first > second:
        return first
    if second > first:
        return second
    if first == second:
        return 0
