import os
# We import sys for the function sys.exit to exit the program at any given point
import sys


def getFileSafely(path):
    if not os.access(path, os.R_OK):
        print("Exit code 1")
        sys.exit(1)
    print("Congratulations! That was a valid file path!")
    return open(path, 'r')

if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    file = getFileSafely(filename)
    # The following line should *NEVER* get executed if `filename` is invalid
    print("Congratulations! You've specified a file that exists!")
    file.close()
