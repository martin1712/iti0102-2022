

"""Example TK."""


def workday_count(days: int) -> int:
    """Great!"""
    a = days // 7
    b = days - 7
    c = 7 - a * 2 + b
    return c


print(workday_count(48))


def sorta_sum(a: int, b: int) -> int:
    """Great!"""
    c = a + b
    if c in range(10, 20):
        return 20
    else:
        return c


print(sorta_sum(5, 56))


def extra_end(s: str) -> str:
    if len(s) >= 2:
        a = (s[-2] + s[-1]) * 3
        return a


print(extra_end("car"))


def last_indices_elements_sum(nums: list) -> int:
    """Great!"""
    a = nums[-1]
    b = nums[-2]
    if a >= len(nums):
        aa = 0
    else:
        aa = a
    if b >= len(nums):
        bb = 0
    else:
        bb = b
    return aa + bb


print(last_indices_elements_sum([0, 1, 7, 2]))


def divisions(numbers: list) -> int:
    """Great!"""
    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                result += 1
    return result


print(divisions([3, 14, 12, 6]))
