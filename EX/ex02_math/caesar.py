


def encode(message: str, shift: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    if message.isalpha():
        for i in range(len(message)):
            result = message[i] + shift