

"""Regex, yay."""
import re


def find_words(text: str) -> list:
    """Great."""
    words = re.findall(r"[ÕÜÖÄ, A-Z][a-z]+", text)
    return words


def find_words_with_vowels(text: str) -> list:
    """Great."""
    words = re.findall(r"[AUEOIÕÜÖÄ][a-z]+", text)
    return words


def find_sentences(text: str) -> list:
    """Great."""
    words = re.findall(r"([ÕÜÖÄA-Z][^\.!?]*[\.!?]+)", text)
    return words


def find_words_from_sentence(sentence: str) -> list:
    """Great."""
    words = re.findall(r"(\w+)", sentence)
    return words


def find_words_from_sentences_only(text: str) -> list:
    """Great."""
    a = find_sentences(text)
    b = str(a)
    words = re.findall(r"(\w+)", b)
    return words


def find_years(text: str) -> list:
    """Great."""
    words = re.findall(r"(?<!\d)\d{4}(?!\d)", text)
    number = [eval(i) for i in words]
    return number


def find_phone_numbers(text: str) -> dict:
    """Great."""
    list_of_numbers = re.findall(r"(\+(?<!\d)\d{3}\s\d{8}|\+(?<!\d)\d{3}\d{8}|\d{7,8})", text)
    new_list = []
    seven_or_eight = []
    d = {}
    for i in list_of_numbers:
        if len(i) == 12:
            new_list.append(" ".join((i[0:4], i[4:])))
        else:
            new_list.append(i)
    for i in new_list:
        if len(i) == 13:
            d[i[0:4]] = [(i[5:])]
            if new_list.count(i[5:]) >= 1:
                d[i[0:4]] = [(i[5:])] * (new_list.count(i[5:]) + 1)
        else:
            if len(i) in [7, 8]:
                seven_or_eight.append(i)
                d[''] = seven_or_eight
    return d


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    return {}


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    return []


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    return []


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    return ()


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    return set()


def find_two_people_with_most_common_hobbies(data: str) -> tuple:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highes number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    return ()


if __name__ == '__main__':
    print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364 +11 1234567 +327 1 11111111"))
    # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364', '1234567', '11111111']}
