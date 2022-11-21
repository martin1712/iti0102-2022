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
        if power < 0:
            pass
        else:
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



class World:
    pass


class Monster:
    pass


if __name__ == "__main__":
    hero = Adventurer("Sander", "Paladin", 50000000, -40)
    friend = Adventurer("Peep", "Druid", 25, 30)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)

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
