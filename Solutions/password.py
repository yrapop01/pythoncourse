"""
    Generate (mainly) random passwords.
"""

import random

def random_password(n):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '01234567890'
    etc = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?'

    sample = (random.sample(upper, 1) +
              random.sample(number, 1) +
              random.sample(etc + upper + number, n - 2))

    random.shuffle(sample)
    return "".join(sample)

if __name__ == "__main__":
    print(random_password(8))
