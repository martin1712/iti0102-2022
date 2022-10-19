

"""Create schedule from the given file."""
import re
import datetime


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    together = {}

    for match in re.finditer(r"((\d\d.\d\d)|(\d\d.\d)|(\d.\d\d)|(\d.\d))\s+([a-z]+|[A-Z][a-z]+)", input_string):
        # Split by non number symbol.
        result = re.split(r"\D+", match.group(1))
        # Join by :.
        result_with_comas = ":".join(result)
        # Convert to pm am time.
        d = datetime.datetime.strptime(result_with_comas, "%H:%M")
        if d.strftime("%I:%M %p") not in together:
            together[d.strftime("%I:%M %p")] = list()
        together[d.strftime("%I:%M %p")].append(match.group(6))
    for key, value in together.items():
        together[key] = list(dict.fromkeys(value))
    for key, value in together.items():
        together[key] = ", ".join(value)


    table = ""
    for i in together:
        if i[0] == "0":
            table += (f"| {i[1:]:<8}  | {together[i]:<20} |\n")
            if i[1:] in table:
                if together[i] not in table:
                    table += together[i]
        else:
            table += (f"| {i:<8}  | {together[i]:<20} |\n")


    return table

















    return "a"


if __name__ == '__main__':
    print(create_schedule_string(" 11:00 wat 11:00 wat teine tekst 11:0 jah ei 10:00 pikktekst 7$53 nice 15@4 wow, 23.09 nice, 07.7 zoo, 0.0 sleep, 00.25 eat, 09:55 work,  11.0 rererere, 11.05 zzz, 10.0 jump"))
