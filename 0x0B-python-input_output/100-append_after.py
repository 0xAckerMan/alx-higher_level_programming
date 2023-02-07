#!/usr/bin/python3
'''
append after(...)
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    func with args
    '''

    text = ''
    with open(filename, 'w') as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as writeto:
        writeto.write(text)
