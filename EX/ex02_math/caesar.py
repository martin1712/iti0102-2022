

alphabet = "abcdefghijklmnopqrstuvwxyz"
def encode(message: str, shift: int) -> str:
    if message.isalpha():
        position = alphabet.find(character)
        new_position = position(position + shift) % 26
        new_character = alphabet[new_position]
        new_message += new_character
