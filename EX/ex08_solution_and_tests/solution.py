

"""Great."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """

    coffe_hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    no_coffe = [18, 19, 20, 21, 22, 23, 24]
    sleep_hours = [1, 2, 3, 4]
    if time in coffe_hours and coffee_needed is True:
        return True
    if time in no_coffe and coffee_needed is False:
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
    pass


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    pass


if __name__ == '__main__':
    print(students_study(1, True))
