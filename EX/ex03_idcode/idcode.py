

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
    while number not in [0, 7, 8]:
        return True
    else:
        return False


def get_gender(number: int) -> str:
    while number not in [2, 4, 6]:
        return "male"
    while number not in [1, 3, 5]:
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if 0 <= year_number < 100:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    if 0 < month_number < 13:
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if 0 < birth_number < 1000:
        return True
    else:
        return False


def is_leap_year(leap_year: int) -> bool:
    if (leap_year % 400 == 0) and (leap_year % 100 == 0):
        return True
    elif (leap_year % 4 == 0) and (leap_year % 100 != 0):
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    if gender_number in [1, 2] and 0 <= year_number < 100:
        return 1800 + year_number
    if gender_number in [3, 4] and 0 <= year_number < 100:
        return 1900 + year_number
    if gender_number in [5, 6] and 0 <= year_number < 100:
        return 2000 + year_number


def get_birth_place(birth_number: int) -> str:
    if 0 < birth_number < 11:
        return "Kuressaare"
    if 10 < birth_number < 20:
        return "Tartu"
    if 20 < birth_number < 221:
        return "Tallinn"
    if 220 < birth_number < 271:
        return "Kohtla-Järve"
    if 270 < birth_number < 371:
        return "Tartu"
    if 370 < birth_number < 421:
        return "Narva"
    if 420 < birth_number < 471:
        return "Pärnu "
    if 470 < birth_number < 711:
        return "Tallinn"
    else:
        return "Wrong input!"









if __name__ == '__main__':
    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"










