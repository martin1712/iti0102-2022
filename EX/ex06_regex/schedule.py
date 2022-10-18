

"""Create schedule from the given file."""
import re
import datetime
from collections import defaultdict

def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    together = {}
    result_of_all_matches = []

    for match in re.finditer(r"((\d\d.\d\d)|(\d\d.\d)|(\d.\d\d)|(\d.\d))\s+([a-z]+|[A-Z][a-z]+)", input_string):
        # Split by non number symbol.
        result = re.split(r"\D+", match.group(1))
        # Join by :.
        result_with_comas = ":".join(result)
        # Convert to pm am time.
        d = datetime.datetime.strptime(result_with_comas, "%H:%M")
        together[d.strftime("%I:%M %p")] = match.group(6)


        table = ""
        for i in together:
            table += (f"| {i}  | {together[i]} |")

        return table


if __name__ == '__main__':
    print(create_schedule_string(" 11:00 wat 11:00 wat teine tekst 11:0 jah ei 10:00 pikktekst 7$53 nice 15@4 wow, 23.09 nice, 07.7 zoo, 0.0 sleep, 00.25 eat, 09:55 work,  11.0 rererere, 11.05 zzz, 10.0 jump"))
