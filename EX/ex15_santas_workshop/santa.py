import urllib.request
import json
import urllib.parse
import urllib.error
from typing import Optional
import csv
import requests


class Gift:
    def __init__(self, name: str, cost: int, production_time: int, weight_in_grams: int):
        self.name = name
        self.weight = weight_in_grams
        self.cost = cost
        self.time = production_time

    def __repr__(self):
        return f"{self.name}"


NAUGHTY_LIST = "naughty_list"
NICE_LIST = "nice_list"
WISHES_LIST = "no_wishes.txt"


class Child:

    def __init__(self):
        self.all_children = []
        self.is_nice = []
        self.is_bad = []
        self.wishes_list = []
        self.gifts = []

    def read_wishes_list(self, filename: str):
        with open(WISHES_LIST, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.wishes_list.append(row)
        return [[x.strip() for x in row] for row in self.wishes_list]

    def create_list_of_all_children(self, wishes: list):
        for i in self.wishes_list:
            if len(i) >= 1:
                self.all_children.append(i[0])
        return self.all_children

    def read_naughty_list(self, filename: str):
        with open(NAUGHTY_LIST, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.is_bad.append(row)
        return [[x.strip() for x in row] for row in self.is_bad]

    def read_nice_list(self, filename: str):
        with open(NICE_LIST, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.is_nice.append(row)
        return [[x.strip() for x in row] for row in self.is_nice]

    def is_nice_child(self, name: str) -> bool:
        for i in self.is_nice:
            if name in i:
                return True
        return False

    def is_naughty_child(self, name: str) -> bool:
        for i in self.is_bad:
            if name in i:
                return True
        return False

    def find_in_wishes_list(self, name: str) -> bool:
        for i in self.wishes_list:
            if name in i:
                return True
        return False

    def get_list_of_gifts(self, name: str) -> list:
        for i in self.wishes_list:
            if name in i:
                i.remove(name)
                return [x.strip() for x in i]


API_URL = "https://cs.ttu.ee/services/xmas/gift?"


class Warehouse:

    def __init__(self):

        self.gifts_list = []

    def get_product_from_factory(self, name: str):
        qs = urllib.parse.quote_plus(str(name))
        try:
            with urllib.request.urlopen(API_URL + "name=" + qs) as f:
                # read all
                contents = f.read()
                # read json to python object
                data = json.loads(contents.decode('utf-8'))
                if data is True:
                    self.gifts_list.append(name)
                return data
        except urllib.error.HTTPError:
            return None


child = Child()
warehouse = Warehouse()


good_list = child.read_nice_list("nice_list")
bad_list = child.read_naughty_list("naughty_list")
wishes_list = child.read_wishes_list("wishes")
all_children = child.create_list_of_all_children(wishes_list)

print(warehouse.get_product_from_factory("Kitten plushie"))


def get_final_result(list_of_children: list) -> list:
    ready_result = []
    for name in list_of_children:
        if child.is_nice_child(name) is True:
            ready_result.append(name)
            gifts = child.get_list_of_gifts(name)
            ready_result.append(gifts)
    return ready_result


print(get_final_result(all_children))
