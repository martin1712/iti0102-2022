

"""Files."""
import csv


def read_file_contents(filename: str) -> str:
    """Great."""
    with open(filename) as f:
        return f.read()


def read_file_contents_to_list(filename: str) -> list:
    """Great."""
    result = []
    with open(filename) as f:
        for row in f:
            result.append(row.rstrip())
    return result


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            result.append(row)
    return result


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, 'w') as f:
        started = False
        for line in lines:
            if started:
                f.write('\n')
            started = True
            f.write(line)


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    with open(dates_filename) as dt_csv:
        new_dict = {}
        dt_dict_r = csv.DictReader(dt_csv, fieldnames=["name", "date"], delimiter=':')
        for row in dt_dict_r:
            if not row["date"]:
                row["date"] = '-'
            new_dict.update({row["name"]: {"date": row["date"]}})
        with open(towns_filename) as city_csv:
            dt_dict_c = csv.DictReader(city_csv, fieldnames=["name", "city"], delimiter=':')
            print(new_dict)
            for row in dt_dict_c:
                if not row["city"]:
                    row["city"] = '-'
                if new_dict.get(row["name"]):
                    new_dict[row["name"]].update({"city": row["city"]})
                else:
                    new_dict.update({row["name"]: {"date": '-', "city": row["city"]}})
        with open(csv_output_filename, "w", newline='') as out_file:
            csv_w = csv.writer(out_file)
            csv_w.writerow(["name", "town", "date"])
            for item in new_dict:
                if not new_dict[item].get("city"):
                    new_dict[item]["city"] = '-'
                csv_w.writerow([item, new_dict[item]["city"], new_dict[item]["date"]])


if __name__ == '__main__':
    # print(read_file_contents("text.txt"))
    # print(read_file_contents_to_list("text.txt"))
    # print(read_csv_file("text.txt"))
    # print(write_contents_to_file("text.txt", "hello"))
    # print(write_lines_to_file("text.txt", ["Hello world", "Its me"]))
    # print(write_csv_file("text.txt", [["name", "age"], ["john", "11"], ["mary", "15"]]))
    print(merge_dates_and_towns_into_csv("dates_filename", "towns_filename", "csv_output_filename"))
