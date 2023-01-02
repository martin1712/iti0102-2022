"""Tests for santa workshop."""
import pytest
from santa import Child
from santa import Warehouse
from santa import Result


@pytest.fixture()
def child():
    return Child()


def test_read_wishes_list_no_wishes(child):
    """Read from empty file."""
    result = child.read_wishes_list("no_wishes.txt")
    assert result == []


def test_read_wishes_list_child_with_wishes_from_naughty_list(child):
    """Read from naughty file."""
    result = child.read_naughty_list("naughty_list")
    assert len(result) == 110
    assert result[0][0] == "Tanya"
    assert result[0][1] == "United Kingdom"


def test_read_wishes_from_file(child):
    """Read from wishes file."""
    result = child.read_wishes_list("wishes")
    assert len(result) == 3


def test_get_list_of_all_children(child):
    """List of children"""
    result = child.create_list_of_all_children(child.read_wishes_list("wishes"))
    assert len(result) == 3


def test_is_nice_child_yes(child):
    """Check if child is good."""
    child.read_nice_list("nice_list")
    assert child.is_nice_child("Evelyn") == True


def test_is_naughty_child_no(child):
    """Check if child is bad."""
    assert child.is_naughty_child("Evelyn") == False


@pytest.fixture()
def warehouse():
    return Warehouse()


def test_get_right_gift_from_factory(warehouse):
    """Get gift from factory."""
    result = warehouse.get_product_from_factory("Kitten plushie")
    assert result['gift'] == 'Kitten plushie'
    assert result['material_cost'] == 10
    assert result['production_time'] == 3
    assert result['weight_in_grams'] == 150


def test_get_wrong_gift_from_factory(warehouse):
    """Wrong gift check."""
    result = warehouse.get_product_from_factory("ferrari portofino")
    assert result is None


@pytest.fixture()
def result():
    return Result()


def test_get_result_three_child(result):
    """Get ready list of good children."""
    child = Child()
    list_of_children = child.create_list_of_all_children(child.read_wishes_list("wishes"))
    result = result.get_final_result(list_of_children)
    assert len(result) == 6
