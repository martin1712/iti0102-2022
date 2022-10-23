

import pytest
from solution import students_study
from solution import lottery
from solution import fruit_order


def test_students_study_evening():
    """Student always studies at evening."""
    assert students_study(24, True) is True
    assert students_study(24, False) is True
    assert students_study(18, True) is True
    assert students_study(18, False) is True


def test_students_study_night_no_study():
    """Student cant study at night."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False


def test_students_study_day_coffe_needed():
    """Student studies during the day only with coffee."""
    assert students_study(5, True) is True
    assert students_study(5, False) is False
    assert students_study(17, True) is True
    assert students_study(17, False) is False


def test_lottery_same_numbers():
    """If all 5, result is 10, with other numbers it is 5."""
    assert lottery(5, 5, 5) == 10
    assert lottery(0, 0, 0) == 5
    assert lottery(-1, -1, -1) == 5
    assert lottery(10, 10, 10) == 5


def test_lottery_two_same_numbers():
    """First number equal to second or third is 0, if second and third are equal it is 1."""
    assert lottery(2, 2, 5) == 0
    assert lottery(7, 4, 7) == 0
    assert lottery(2, 7, 7) == 1


def test_lottery_all_different_number():
    """With all different numbers answer is 1."""
    assert lottery(1, 3, 5) == 1


def test_fruit_order_zero_amount_of_something():
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(1, 1, 0) == 0


def test_fruit_order_big_basket():
    assert fruit_order(0, 3, 15) == 0
    assert fruit_order(0, 2, 15) == -1
    assert fruit_order(0, 3, 10) == 0
    assert fruit_order(0, 3, 9) == 0


