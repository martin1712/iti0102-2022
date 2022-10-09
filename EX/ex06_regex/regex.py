

"""Regex, yay."""
import re



def find_words(text: str) -> list:
    words = re.findall(r"[ÕÜÖÄ, A-Z][a-z]+", text)
    return words


def find_words_with_vowels(text: str) -> list:
    words = re.findall(r"[AUEOIÕÜÖÄ][a-z]+", text)
    return words


def find_sentences(text: str) -> list:
    words = re.findall(r"([ÕÜÖÄA-Z][^\.!?]*[\.!?]+)", text)
    return words


def find_words_from_sentence(sentence: str) -> list:
    words = re.findall(r"(\w+)", sentence)
    return words


def find_words_from_sentences_only(text: str) -> list:
    a = find_sentences(text)
    b = str(a)
    words = re.findall(r"(\w+)", b)
    return words

def find_years(text: str) -> list:
    words = re.findall(r"(?<!\d)\d{4}(?!\d)", text)
    number = [eval(i) for i in words]
    return number



def find_phone_numbers(text: str) -> dict:

    list_of_numbers = re.findall(r"(\+(?<!\d)\d{3}\s\d{8}|\+(?<!\d)\d{3}\d{8}|\d{7,8})", text)
    from_list_to_string = str(list_of_numbers)

    print(type(from_list_to_string))

    return {}



if __name__ == '__main__':
    print(find_words('KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))
    # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
    print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAAhven'))
    # ['Apelsin', 'Õun', 'Ahven']
    print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']
    print(find_words_from_sentence("Super lause ää, sorry."))
    # ['Super', 'lause', 'ää', 'sorry']
    print(find_words_from_sentences_only('See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See', 'on', 'esimene', 'ä', 'lause', 'See', 'on', 'teine', 'lause', 'Aga', 'kas', 'see', 'on']
    print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))
    # [1998, 7777]
    print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364 +11 1234567 +327 1 11111111"))
    # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364', '1234567', '11111111']}