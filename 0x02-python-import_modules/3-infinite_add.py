#!/usr/bin/python3
from sys import argv


def add():
    length = len(argv)
    if length == 1:
        return 0

    sum = 0
    index = 1
    while index < length:
        sum += int(argv[index])
        index += 1

    return sum


if __name__ == '__main__':
    print(add())
