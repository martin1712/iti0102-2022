

"""Caesar program."""

def encode(message: str, shift: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    ord_first_letter_lower = ord("a")
    for i in message:
        if i in alphabet:
            result += chr(((ord(i) - ord_first_letter_lower + shift) % 26) + ord_first_letter_lower)
        else:
            result += i

    return result

print(encode("dog eats", 5))