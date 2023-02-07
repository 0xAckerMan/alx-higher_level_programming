#!/usr/bin/python3
'''
reads and write in a file
'''


def write_file(filename="", text=""):
    ''' the function'''

    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
