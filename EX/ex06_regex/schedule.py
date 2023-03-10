

"""Create schedule from the given file."""
import re
from datetime import datetime


def number_convert_time(number: int) -> str:
    """Nice."""
    result = '{:02d}:{:02d}'.format(*divmod(number, 60))
    return result


def convert_to_pm_am(number: int) -> str:
    """Nice."""
    a = number_convert_time(number)
    d = datetime.strptime(a, "%H:%M")
    if d.strftime("%I:%M %p")[0] == "0":
        return d.strftime("%I:%M %p")[1:]
    else:
        return d.strftime("%I:%M %p")


def find_the_longest_key(dictionary: dict) -> int:
    """Holy."""
    list_of_times = []
    for i in dictionary:
        if convert_to_pm_am(i) not in list_of_times:
            list_of_times.append(convert_to_pm_am(i))
    x = len(max(list_of_times, key=len))
    return x


def find_the_longest_value(dictionary: dict) -> int:
    """Holy."""
    list_of_action = []
    for i in dictionary:
        if dictionary[i] not in list_of_action:
            list_of_action.append(dictionary[i])
    x = len(max(list_of_action, key=len))
    return x


def create_table(d: dict) -> str:
    """Create table."""
    table = ""
    x = find_the_longest_value(d)
    y = find_the_longest_key(d)
    if x >= 7:
        z = ("-" * (x + y + 7))
        table += f"{z}\n"
        table += f"| {'time':>{y}} | {'entries':<{x}} |\n"
        z = ("-" * (x + y + 7))
        table += f"{z}\n"
        for row in d:
            table += f"| {convert_to_pm_am(row):>{y}} | {d[row]:<{x}} |\n"
        table += f"{z}\n"
        return table
    if x < 7:
        z = ("-" * (y + 14))
        table += f"{z}\n"
        table += f"| {'time':>{y}} | {'entries':<{7}} |\n"
        z = ("-" * (y + 14))
        table += f"{z}\n"
        for row in d:
            table += f"| {convert_to_pm_am(row):>{y}} | {d[row]:<{7}} |\n"
            z = ("-" * (y + 14))
        table += f"{z}\n"
        return table


def create_table_none() -> str:
    """Sus."""
    table = ""
    z = ("-" * 20)
    table += f"{z}\n"
    table += f"| {'time':>{5}} | {'entries':<{8}} |\n"
    table += f"{z}\n"
    table += f"| {'No entries found'} |\n"
    table += f"{z}\n"
    return table


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    together = {}
    if re.search(r"(\s+)(\d\d[^0-9]\d\d|\d\d[^0-9]\d|\d[^0-9]\d\d|\d[^0-9]\d)\s+([a-zA-Z]+)", input_string) is not None:
        for match in re.finditer(r"(\s+)(\d\d[^0-9]\d\d|\d\d[^0-9]\d|\d[^0-9]\d\d|\d[^0-9]\d)\s+([a-zA-Z]+)", input_string):
            # Lower words.
            lower_words = match.group(3).lower()
            # Split by non number symbol.
            result = re.split(r"\D+", str(match.group(2)))
            # Adding 0.
            result[0] = result[0].zfill(2)
            result[1] = result[1].zfill(2)
            # Join by :.
            result_with_comas = ":".join(result)
            # Transform time to minutes.
            if int(result_with_comas[:2]) <= 23 and int(result_with_comas[3:]) <= 59:
                result_in_minutes = int(result_with_comas[:2]) * 60 + int(result_with_comas[3:])
                if result_in_minutes not in together:
                    together[result_in_minutes] = list()
                together[result_in_minutes].append(lower_words)
        for key, value in together.items():
            together[key] = list(dict.fromkeys(value))
        for key, value in together.items():
            together[key] = ", ".join(value)
        # Sort dict by key.
        d_sorted = {key: value for key, value in sorted(together.items(), key=lambda item: int(item[0]))}
        tabel = create_table(d_sorted)
        return tabel
    else:
        sus = create_table_none()
        return sus


if __name__ == '__main__':
    print(create_schedule_string("7"))
