

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
    if 10 < birth_number < 21:
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
        return "Pärnu"
    if 470 < birth_number < 711:
        return "Tallinn"
    if 710 < birth_number < 1000:
        return "undefined"
    else:
        return "Wrong input!"


def is_valid_control_number(id_code: str) -> bool:
    result = ""
    for i in id_code:
        if i.isdigit():
            result += i
    a = len(result)
    if a != 11:
        return False
    b = int(result[0]) * 1 + int(result[1]) * 2 + int(result[2]) * 3 + int(result[3]) * 4 + int(result[4]) * 5 + int(
        result[5]) * 6 + int(result[6]) * 7 + int(result[7]) * 8 + int(result[8]) * 9 + int(result[9]) * 1
    if b % 11 == int(result[10]):
        return True
    c = int(result[0]) * 3 + int(result[1]) * 4 + int(result[2]) * 5 + int(result[3]) * 6 + int(result[4]) * 7 + int(
        result[5]) * 8 + int(result[6]) * 9 + int(result[7]) * 1 + int(result[8]) * 2 + int(result[9]) * 3
    if b % 11 != int(result[10]) and c % 11 == int(result[10]):
        return True
    elif c % 11 == 0:
        return True
    elif b % 11 < 10 and b != int(result[10]):
        return False
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    if day_number > 31:
        return False
    if month_number == 2:
        full_year = get_full_year(gender_number, year_number)
        leap_year = is_leap_year(full_year)
        if leap_year is True and day_number <= 29:
            return True
        if leap_year is True and day_number > 29:
            return False
        if leap_year is False and day_number <= 28:
            return True
        if leap_year is False and day_number > 28:
            return False
    if month_number in [4, 6, 9, 11] and day_number > 30:
        return False
    else:
        return True


def is_id_valid(id_code: str) -> bool:
    if find_id_code(id_code) != 11:
        return False
    gender_number = int(id_code[0])
    year_number = int(id_code[1:3])
    month_number = int(id_code[3:5])
    day_number = int(id_code[5:7])
    birth_number = int(id_code[7:10])
    control_number = (id_code[10])
    if is_valid_gender_number(gender_number) and is_valid_year_number(year_number) and is_valid_month_number(month_number) and is_valid_day_number(day_number) and is_valid_birth_number(birth_number) and is_valid_control_number(control_number) is True:
        return True
    else:
        return False


def get_data_from_id(id_code: str) -> str:
    if is_id_valid is True:
        gender = int(id_code)
        gender_number = int(id_code[0])
        year_number = int(id_code[1:3])
        day_number = int(id_code[5:7])
        month_number = int(id_code[3:5])
        birth_place = int(id_code[7:10])
        full_year = get_full_year(gender_number, year_number)
        return f"This is a {get_gender(gender)} born on {day_number}.{month_number}.{get_full_year(full_year)} in {get_birth_place(birth_place)}"
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
