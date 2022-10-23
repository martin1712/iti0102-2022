

import pytest
from solution import students_study
from solution import lottery


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
    assert lottery(5, 5, 5) is 10
    assert lottery(0, 0, 0) is 5
    assert lottery(-1, -1, -1) is 5
    assert lottery(10, 10, 10) is 5
