import urllib.request
import json
import urllib.parse
import urllib.error
from typing import Optional
import csv


class Gift:
    def __init__(self, name: str, cost: int, production_time: int, weight_in_grams: int):
        self.name = name
        self.weight = weight_in_grams
        self.cost = cost
        self.time = production_time

    def __repr__(self):
        return f"Gift: {self.name} ({self.weight}g)"


API_URL = "https://cs.ttu.ee/services/xmas/gift?"


class Warehouse:

    def __init__(self):
        self.gifts: dict[str, int] = {}
        self.gifts: dict[str, Gift] = {}
        self.gifts_list = []

    def get_product_from_factory(self, name: str) -> Optional[Gift]:
        qs = urllib.parse.quote_plus(name)
        try:
            with urllib.request.urlopen(API_URL + "name=" + qs) as f:
                # read all
                contents = f.read()

                # to convert into regular string
                print(contents.decode("utf-8"))

                # read json to python object
                data = json.loads(contents.decode('utf-8'))
                print(data)

                gift = Gift(data['gift'], data['material_cost'],
                            data['production_time'], data['weight_in_grams'])

                if data['gift'] not in self.gifts:
                    self.gifts[data['gift']] = []
                self.gifts[data['gift']].append(Gift)
                return gift
        except urllib.error.HTTPError:
            return None

    def get_list_of_gifts(self, name: str) -> list:


        pass


NAUGHTY_LIST = "naughty_list"
NICE_LIST = "nice_list"
WISHES_LIST = "wishes"


class Child:

    def __init__(self):
        self.is_nice = []
        self.is_bad = []
        self.wishes_list = []
        self.gifts = []
        ready_result = {}

    def read_wishes_list(self, filename: str):
        with open(WISHES_LIST, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.wishes_list.append(row)
        return [[x.strip() for x in row] for row in self.wishes_list]

    def create_list_of_gifts(self, wishes: list) -> list:
        for i in wishes:
            del i[0]
        return wishes

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
                del i[0]
            return i



warehouse = Warehouse()
ready_result = {}
child = Child()
warehouse = Warehouse()

good_list = child.read_nice_list("nice_list")
bad_list = child.read_naughty_list("naughty_list")
wishes_list = child.read_wishes_list("wishes")

# print(warehouse.get_product_from_factory("Lego death star"))
# print(child.is_nice_child("Libby"))
# print(child.create_list_of_gifts(wishes_list))
print(child.get_list_of_gifts("Libby"))

child_name = "Libby"

if child.is_nice_child(child_name) and child.find_in_wishes_list(child_name) is True:
    gifts = child.get_list_of_gifts(child_name)
    for i in gifts:






print(good_list)
print(bad_list)



# print(child.read_nice_list("nice_list"))
# print(child.read_naughty_list("naughty_list"))
# print(warehouse.get_product_from_factory("cyberpunk 2077"))

