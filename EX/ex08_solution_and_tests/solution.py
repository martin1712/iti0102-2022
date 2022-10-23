

"""Great."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    coffe_hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    no_coffe = [18, 19, 20, 21, 22, 23, 24]
    if time in coffe_hours and coffee_needed is True:
        return True
    if time in no_coffe and coffee_needed is False:
        return True
    if time in no_coffe and coffee_needed is False:
        return True
    if time in no_coffe and coffee_needed is True:
        return True
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    if a == b == c:
        if a != 5 and b != 5 and c != 5:
            return 5
    if a != b and a != c:
        return 1
    if a == b != c or a == c != b:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    x = big_baskets * 5
    if x + small_baskets == ordered_amount:
        return small_baskets
    if x + small_baskets <= ordered_amount:
        return -1
    if x + small_baskets >= ordered_amount:
        if x == ordered_amount:
            return 0
        if x != ordered_amount:
            if small_baskets >= ordered_amount:
                return ordered_amount
            if small_baskets <= ordered_amount:
                return small_baskets
            else:
                return small_baskets + x - ordered_amount


if __name__ == '__main__':
    print(students_study(18, True))
    print(lottery(0, 0, 0))
    print(fruit_order(1, 5, 21))
