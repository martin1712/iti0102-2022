


def encode(message: str, shift: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if message.isalpha():
        for i in range(alphabet, shift):

