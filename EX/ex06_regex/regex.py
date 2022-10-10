

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


if __name__ == '__main__':
    print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364 +11 1234567 +327 1 11111111"))
    # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364', '1234567', '11111111']}
