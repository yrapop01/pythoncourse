"""
    Print modified time for a file passed as argument
"""
    
import os

import stat
import time
import argparse

def print_modified(path):
    st = os.stat(path)
    print(time.ctime(st[stat.ST_MTIME]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='file path')
    args = parser.parse_args()

    print_modified(args.path)
