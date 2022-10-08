

"""TK3."""


def common_end(a: list, b: list) -> bool:
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.

    Both lists will be length 1 or more.

    common_end([1, 2, 3], [7, 3]) → True
    common_end([1, 2, 3], [7, 3, 2]) → False
    common_end([1, 2, 3], [1, 3]) → True
    :param a: List of integers.
    :param b: List of integers.
    :return: The last or the first elements are the same.
    """
    if len(a) and len(b) >= 1:
        if a[0] == b[0] or a[-1] == b[-1]:
            return True
        if a[-1] == b[-1]:
            return True
        else:
            return False


def alarm_clock(day: int, vacation: bool) -> str:
    """
    Return what time the alarm clock should be set.

    Given a day of the week encoded as 0=Mon, 1=Tue, ... 5=Sat, 6=Sun
    and a boolean indicating if we are on vacation,
    return a string of the form "08:00" indicating when the alarm clock should ring.

    Weekdays, the alarm should be "08:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

    alarm_clock(1, False) → '08:00'
    alarm_clock(3, False) → '08:00'
    alarm_clock(6, False) → '10:00'
    alarm_clock(6, True) → 'off'

    :param day: Day of week.
    :param vacation: Whether it is vacation.
    :return: String when to set alarm clock.
    """
    if vacation is False:
        if day in [0, 1, 2, 3, 4]:
            return "08:00"
        if day in [5, 6]:
            return "10:00"
    if vacation is True:
        if day in [0, 1, 2, 3, 4]:
            return "10:00"
        if day in [5, 6]:
            return "off"


def sum_of_a_beach(s: str) -> int:
    """
    Count how many beach elements are in the string.

    Beaches are filled with sand, water, fish, and sun.
    Given a string, calculate how many times the words
    “Sand”, “Water”, “Fish”, and “Sun” appear without
    overlapping (regardless of the case).

    sum_of_a_beach("WAtErSlIde")                    ==>  1
    sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
    sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
    sum_of_a_beach("cItYTowNcARShoW")               ==>  0
    """
    string_lower = s.lower()
    a = string_lower.count("sand")
    b = string_lower.count("water")
    c = string_lower.count("fish")
    d = string_lower.count("sun")
    return a + b + c + d


def min_index_value(nums: list) -> int:
    """
    Take the first and the last element as indices of two elements and return the smaller of those elements.

    If at least one index is out of range, return -1.
    All the values are non-negative integers.

    min_index_value([1, 2, 3]) => -1 (3 is out of range)
    min_index_value([1, 2, 1]) => 2 (both elements point to 2)
    min_index_value([1, 2, 0]) => 1 (have to take minimum of 2 and 1)
    min_index_value([1, 2, 0, 3]) => 2 (have to take minimum of 2 and 3)

    :param nums: List of non-negative integers.
    :return: Minimum value of two elements at positions of the first and the last element value.
    """
    a = nums[0]
    b = nums[-1]
    if a >= len(nums):
        return -1
    if b >= len(nums):
        return -1
    else:
        return min(nums[a], nums[b])
