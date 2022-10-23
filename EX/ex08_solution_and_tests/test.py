

import pytest
from solution import students_study


def test_students_study_evening():
    assert students_study(20, True) is True
    assert students_study(20, False) is True
    assert students_study(24, True) is False
    assert students_study(17, False) is False


def test_students_study_night_no_study():
    assert students_study(2, True) is False
    assert students_study(2, False) is False


def test_students_study_day_coffe_needed():
    assert students_study(8, True) is True
    assert students_study(8, False) is False


def test_students_study_evening_edge():
    assert students_study(1, True) is False
    assert students_study(17, False) is False
