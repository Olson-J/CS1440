import os
import sys

def getFileSafely(path):
    if not os.access(path, os.R_OK):
        print("Exit code 1")
        sys.exit(1)
    return open(path, 'r')
    pass

def printContents1(file):
    text = file.read()
    print(text, end='')
    pass


def printContents2(file):
    for lines in file:
        print(lines, end='')
    pass


def printTwice(filename):
    f = getFileSafely(filename)
    printContents1(f)
    f.seek(0)
    printContents2(f)
    f.close()
    pass

if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    printTwice(filename)
