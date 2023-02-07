#!/usr/bin/python3
'''
appends a string at the end of a text file and returns the number of char added
'''


def append_write(filename="", text=""):
    '''Func implementation'''

    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
