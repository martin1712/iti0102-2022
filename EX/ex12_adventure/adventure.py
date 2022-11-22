"""Rpg."""


class Adventurer:
    """Adventurer class, wow."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Information about adventurers."""
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
    """Rules of the world."""

    def __init__(self, python_master: str):
        """Information and the name of creator."""
        self.python_master = python_master
        self.graveyard = []
        self.adventurers = []
        self.monsters = []

    def get_python_master(self):
        """Get python master."""
        return self.python_master

    def get_graveyard(self):
        """Get graveyard."""
        return self.graveyard

    def get_adventurer_list(self):
        """Get adventurers."""
        return self.adventurers

    def get_monster_list(self):
        """Get monsters."""
        return self.monsters

    def add_adventurer(self, hero: Adventurer):
        """Add adventurer."""
        if isinstance(hero, Adventurer):
            self.adventurers.append(hero)

    def add_monster(self, monster: Monster):
        """Add monster."""
        if isinstance(monster, Monster):
            self.monsters.append(monster)
