

"""Is_prime_number."""

def is_prime_number(number: int) -> bool:
    """1 and 0 are not prime numbers."""
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True
