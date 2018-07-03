"""
    Run divisors.py from another process.
"""

import subprocess
import sys

def main():
    for line in sys.stdin:
        args = ['python3', 'divisors.py', line.strip()]
        output = subprocess.check_output(args)
        print(str(output, 'ascii'))

if __name__ == "__main__":
    main()
