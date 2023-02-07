#!/usr/bin/python3
'''
Reads a utf8 file and prints it in stdout
'''


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
