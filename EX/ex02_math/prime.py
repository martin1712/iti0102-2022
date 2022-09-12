

def is_prime_number(number: int) -> bool:
    if number > 1:
        x = number / 2
        if x is not int:
            return True
    else: return False
