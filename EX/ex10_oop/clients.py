"""Client."""
from typing import Optional
import csv


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount
        self.earnings_per_day = (self.current_amount - self.starting_amount) / self.account_age

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        return (self.starting_amount - self.current_amount) / self.account_age


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            result.append(Client(row[0], row[1], int(row[2]), int(row[3]), int(row[4])))
    return result


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if bank in row[1]:
                result.append(Client(row[0], row[1], int(row[2]), int(row[3]), int(row[4])))
    return result


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (int(row[4]) - int(row[3])) / int(row[2]) > 0:
                result.append(Client(row[0], row[1], int(row[2]), int(row[3]), int(row[4])))
    if len(result) == 0:
        return None
    else:
        sorted_result = sorted(sorted(result, key=lambda x: x.account_age), key=lambda x: x.earnings_per_day, reverse=True)
        return sorted_result[0]


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (int(row[4]) - int(row[3])) / int(row[2]) < 0:
                result.append(Client(row[0], row[1], int(row[2]), int(row[3]), int(row[4])))
    if len(result) == 0:
        return None
    else:
        sorted_result = sorted(sorted(result, key=lambda x: x.account_age), key=lambda x: x.earnings_per_day)
        return sorted_result[0]


if __name__ == '__main__':
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
