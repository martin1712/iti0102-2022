"""Hobbies but OOP."""


class Person:
    """
    Class for people.

    Every person has
    a first name,
    last name and
    list of hobbies.
    """

    def __init__(self, first_name: str, last_name: str, hobbies: list):
        """
        Person constructor.

        :param first_name: first name of the person
        :param last_name: last name of the person
        :param hobbies: list of hobbies
        """
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return str(self.first_name) + str(self.last_name)

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    result = []
    for i in people_list:
        if hobby in i.hobbies:
            result.append(i)
    return result


def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    result = []
    for i in people_list:
        result.insert(0, i)
    sorted_list = sorted(result, key=lambda x: len(x.hobbies), reverse=True)
    return sorted_list


def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    result = []
    for i in people_list:
        result.insert(0, i)
    sorted_list = sorted(result, key=lambda x: len(x.hobbies))
    return sorted_list


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return a list of people but sorted alphabetically by their full name.

    Also sort their list of hobbies alphabetically.

    : param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_list = sorted(people_list, key=lambda x: x.full_name)
    for i in people_list:
        i.hobbies.sort()
    return sorted_list


if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "Ananas", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space"])
    person4 = Person("Arti", "Sunny", ["eat", "biking"])
    people = [person1, person2, person3, person4]

    print(sort_people_and_hobbies(people))  # -> [ElonMusk, JeffBezos, MariKukk]
    print(person4.hobbies)  # -> ['biking', 'dancing', 'programming']
