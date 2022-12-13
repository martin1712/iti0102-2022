import requests


class GiftDatabase:
    def __init__(self, url_prefix: str):
        self.url_prefix = url_prefix
        self.gifts: dict[str, dict] = {}

    def __get_gift_from_api(self, name):
        url = self.url_prefix + name
        response = requests.get(url)
        self.gifts[name] = response.json()
        return self.gifts[name]

    def get_gifts(self, name):
        if name in self.gifts:
            return self.gifts[name]
        return self.__get_gift_from_api(name)


class Child:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.is_nice = True
        self.wishlists = []
    pass

class Gift:
    def __init__(self, name: str):
        self.name = name
        self.weight = 10
        self.price = 10
        self.time = 10


class Storage:
    def __init__(self):
        self.gifts_counts = dict[str, int] = {}
        self.gifts: dict[str, Gift] = {}
        self.gifts_list = []

    def get_gift(self, gift: Gift):
        id(gift)


class World:
    def __init__(self):
        self.children = {}
        self.nice_children = []
        self.naughty_children = []

        # "kati": ["karu", "kiisu"]
        self.wishlist: dict[str, list[str]] = {}
        self.gifts_db = GiftDatabase("https://cs.ttu.ee/services/xmas/gift?name=swimming%20flippers")

    def parse_nice_list(self, filename: str):
        pass

    def parse_wishlist(self, filename: str):
        pass


if __name__ == '__main__':
    pass