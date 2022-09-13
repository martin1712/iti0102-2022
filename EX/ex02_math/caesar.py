


def encode(message: str, shift: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in message:
        place = alphabet.find(i)
        new_place = place + shift
        if i in alphabet:
            return alphabet[new_place]
        else:
            i
