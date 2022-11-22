"""Rpg"""


class Adventurer:
    """Adventurer class, wow."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Data"""
        self.name = name
        if class_type not in ["Druid", "Wizard", "Paladin"]:
            class_type = "Fighter"
        self.class_type = class_type
        if power > 99:
            power = 10
        self.power = power

        self.experience = max(0, experience)

    def __repr__(self):
        """How to represent data."""
        return f'{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}.'

    def add_power(self, power: int):
        """Power."""
        self.power += power

    def add_experience(self, exp: int):
        """Exp."""
        if exp < 0:
            pass
        else:
            self.experience += exp
            if self.experience > 99:
                self.power += self.experience // 10
                self.experience = 0


class Monster:
    """Monster class."""

    def __init__(self, name: str, type: str, power: int):
        """Monster data."""
        self.power = power
        if type == "Zombie":
            name = "Undead " + name
        self.type = type
        self.name = name

    def __repr__(self):
        """How to represent data."""
        return f"{self.name} of type {self.type}, Power: {self.power}."

class World:
    """World class."""
    def __init__(self, python_master: str):
        self.python_master = python_master
        self.graveyard = []
        self.adventurers = []
        self.monsters = []

    def get_python_master(self):
        return self.python_master

    def get_graveyard(self):
        return self.graveyard

    def get_adventurers(self):
        return self.adventurers

    def get_monsters(self):
        return self.monsters


if __name__ == "__main__":
    hero = Adventurer("Sander", "Paladin", 50000000, -40)
    friend = Adventurer("Peep", "Druid", 25, 30)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    # riend.add_experience(500)
    friend.add_experience(-20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()
