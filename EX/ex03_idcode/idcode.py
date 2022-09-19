

"""Great!"""


def find_id_code(text: str) -> str:
    result = ""
    for i in text:
        if i.isdigit():
            result += i
    a = len(result)
    if a < 11:
        return "Not enough numbers!"
    if a > 11:
        return "Too many numbers!"
    else:
        return result


def the_first_control_number_algorithm(text: str) -> str:
    result = ""
    for i in text:
        if i.isdigit():
            result += i
    a = len(result)
    if a != 11:
        return "Incorrect ID code!"
    b = int(result[0]) * 1 + int(result[1]) * 2 + int(result[2]) * 3 + int(result[3]) * 4 + int(result[4]) * 5 + int(
        result[5]) * 6 + int(result[6]) * 7 + int(result[7]) * 8 + int(result[8]) * 9 + int(result[9]) * 1
    if b % 11 == int(result[10]):
        return result
    elif b % 11 >= 10:
        return "Needs the second algorithm!"
    elif b % 11 < 10 and b != int(result[10]):
        return "Incorrect ID code!"


def is_valid_gender_number(number: int) -> bool:
    if number == [1, 2, 3, 4, 5, 6]:
        return True
    else:
        return False


def get_gender(number: int) -> str:
    if number == [2, 4, 6]:
        return "female"
    if number == [1, 3, 5]:
        return "male"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    return year_number < 100


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    return month_number < 13



def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    return birth_number < 32


