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
        return f"{[self.name]}, the {[self.class_type]}, Power: {[self.power]}, Experience: {[self.experience]}."

    def add_power(self, power: int):
        """Power."""
        return self.power + power

    def add_experience(self, exp: int):
        """Exp."""
        result = self.experience + exp
        if result > 99:
            self.power = self.power + result // 10
            self.experience = 0
        return result
