

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
        a = match.group(1).split(":")
        if int(a[0]) <= 23 and int(a[1]) <= 59:
            d = datetime.datetime.strptime(match.group(1), "%H:%M")
            together[d.strftime("%I:%M %p")] = match.group(6)
        print(together)
    for i in together:

        print(f"| {i:>20}  | {together[i]:>10} |")
    return "a"



if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst 23:45 ok 01:01 okidoki 55:444 wow "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")