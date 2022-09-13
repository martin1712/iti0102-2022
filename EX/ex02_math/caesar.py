

def encode(message: str, shift: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in message:
        if i in alphabet:
            result += chr(ord(i) + shift)
        else:
            result += i

    return result
