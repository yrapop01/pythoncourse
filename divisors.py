"""
    Calculate prime factors of a number.
"""

import argparse

def print_divisors(n):
    """Print all prime divisors of a number"""

    assert n > 0, "The given number is not natural"

    i = 2
    while i <= n:
        if n % i == 0:
            yield i
        while n % i == 0:
            n //= i
        i += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="an integer", type=int)
    args = parser.parse_args()

    for i in print_divisors(args.n):
        print(i)
