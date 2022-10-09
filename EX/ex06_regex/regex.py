

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

    pass


def find_years(text: str) -> list:

    pass


def find_phone_numbers(text: str) -> dict:

    pass


if __name__ == '__main__':
    print(find_words('KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))
    # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
    print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAAhven'))
    # ['Apelsin', 'Õun', 'Ahven']
    print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']
    print(find_words_from_sentence("Super lause ää, sorry."))
    # ['Super', 'lause', 'ää', 'sorry']