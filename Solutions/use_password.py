"""
    Use random password generator defined in another module.
"""

from password import random_password
import argparse

def main():
    parser = argparse.ArgumentParser()

    args = parser.add_argument('n', type=int, choices=range(2, 101))
    args = parser.parse_args()

    print(random_password(args.n))

if __name__ == "__main__":
    main()
