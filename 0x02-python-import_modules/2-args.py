#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print(f"{1:d}: {argv[1]:s}")
    else:
        print(f"{len(argv)-1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i:d}: {argv[i]:s}")