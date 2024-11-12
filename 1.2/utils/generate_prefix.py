from random import choice
from string import ascii_lowercase


def generate_prefix(lenght: int = 6) -> str:
    prefix = ""
    alph = ascii_lowercase + "0123456789"

    for _ in range(lenght):
        prefix += choice(alph)
    
    return prefix
