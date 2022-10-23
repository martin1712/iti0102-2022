

import pytest
from solution import students_study


def test_students_study_evening():
    assert students_study(24, True) is True
    assert students_study(24, False) is True
    assert students_study(18, True) is True
    assert students_study(18, False) is True


def test_students_study_night_no_study():
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False


def test_students_study_day_coffe_needed():
    assert students_study(5, True) is True
    assert students_study(5, False) is False
    assert students_study(17, True) is True
    assert students_study(17, False) is False
