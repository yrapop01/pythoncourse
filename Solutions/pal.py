"""
    Print for every line in stdin if it's palindrome or not.
"""

import sys

def main():
    for line in sys.stdin:
        s = line.strip()
        n = len(s)

        print(s[:n // 2 + 1] == s[::-1][:n // 2 + 1])

if __name__ == "__main__":
    main()
