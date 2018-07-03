import argparse
import sys
import os
import re

def ls(path):
    result = []
    for root, directories, files in os.walk(path):
        for fl in files:
            result.append(root + '/' + fl)
    return result
       
def grep(regex, files_list, max_string=255):
    rgx = re.compile(regex)
    result = []
    for fullname in files_list:
        try:
            with open(fullname) as text:
                lines = text.readlines()
            for i, line in enumerate(lines):
                if rgx.search(line):
                    result.append((fullname, i, line[:max_string].strip()))
        except (UnicodeDecodeError, FileNotFoundError):
            print(fullname, 'is not a text file')
    return result

def run_grep(regex, path):
    files = ls(path)
    matches = grep(regex, files)
    for filename, i, line in matches:
        print('{}:{}\t{}...'.format(filename, i, line))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='search root path')
    parser.add_argument('regex', help='regex to look up for')

    args = parser.parse_args()
    run_grep(args.regex, args.path)















