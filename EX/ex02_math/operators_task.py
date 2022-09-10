

def add(x: int, y: int):
    x + y
    return x + y

def sub(x: int, y: int):
    x - y
    return x - y

def multiply(x: int, y: int):
    x * y
    return x * y

def div(x: int, y: int):
    x / y
    return x / y

def modulus(x: int, y: int):
    x % y
    return x % y

def floor_div(x: int, y: int):
    x // y
    return x // y

def exponent(x: int, y: int):
    x ** y
    return x ** y

def first_greater_or_equal(x: int, y: int):
    x >= y
    return x >= y

def second_less_or_equal(x: int, y: int):
    x <= y
    return x <= y

def x_is_y(x: int, y: int):
    x == y
    return x == y

def x_is_not_y(x: int, y: int):
    x != y
    return x != y

def if_else(a: int, b: int, c: int, d: int):
    first = a * b
    second = c / d
    if first > second:
        return first
    if second > first:
        return second
    if first == second:
        return 0

