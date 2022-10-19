

"""Create schedule from the given file."""
import re
from datetime import datetime


def number_convert_time(number: int) -> str:
    result = '{:02d}:{:02d}'.format(*divmod(number, 60))
    return result


def convert_to_pm_am(number: int) -> str:
    a = number_convert_time(number)
    d = datetime.strptime(a, "%H:%M")
    if d.strftime("%I:%M %p")[0] == "0":
        return d.strftime("%I:%M %p")[1:]
    else:
        return d.strftime("%I:%M %p")


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    together = {}
    for match in re.finditer(r"((\d\d.\d\d)|(\d\d.\d)|(\d.\d\d)|(\d.\d))\s+([a-z]+|[A-Z][a-z]+)", input_string):
        # Split by non number symbol.
        result = re.split(r"\D+", match.group(1))
        # Adding 0.
        result[0] = result[0].zfill(2)
        result[1] = result[1].zfill(2)
        print(result[1])
        # Join by :.
        result_with_comas = ":".join(result)
        # Transform time to minutes.
        if int(result_with_comas[:2]) <= 23 and int(result_with_comas[3:]) <= 59:
            result_in_minutes = int(result_with_comas[:2]) * 60 + int(result_with_comas[4:5])
            if result_in_minutes not in together and int(result_with_comas[:2]) <= 23 and int(result_with_comas[3:]) <= 59:
                together[result_in_minutes] = list()
            together[result_in_minutes].append(match.group(6))
    for key, value in together.items():
        together[key] = list(dict.fromkeys(value))
    for key, value in together.items():
        together[key] = ", ".join(value)
    # Sort dict by key.
    d_sorted = {key: value for key, value in sorted(together.items(), key=lambda item: int(item[0]))}
    list_of_times = []
    list_of_action = []
    for i in d_sorted:
        if d_sorted[i] not in list_of_action:
            list_of_action.append(d_sorted[i])
        if convert_to_pm_am(i) not in list_of_times:
            list_of_times.append(convert_to_pm_am(i))
    for i in d_sorted:
        x = len(max(list_of_action, key=len))
        y = len(max(list_of_times, key=len))
    table_width = x + y + 7
    z = ("-" * table_width)
    table = ""
    table += f"{z}\n"
    table += (f"| {'time':>{y}} | {'entries':<{x}} |\n")
    table += f"{z}\n"
    for i in d_sorted:
        table += (f"| {convert_to_pm_am(i):>{y}} | {d_sorted[i]:<{x}} |\n")
    table += z
    return table


if __name__ == '__main__':
    print(create_schedule_string(" 11:00 wat 11:0 sus teine tekst 1:0 jah ei 10:00 pikktekst 7$53 mimmi 15@4 wow, 298.99 nice, 28.7 zoo, 0.0 sleep, 00.9 eat, 09:55 work,  11.0 rererere, 11.05 zzz, 10.0 jump, 17:3 sing"))
    # print(convert_to_pm_am(444))
