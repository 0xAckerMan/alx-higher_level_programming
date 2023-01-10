#!/usr/bin/python3
def no_c(my_string):
    '''list_string = list(my_string)
    for i in list_string:
        if i == 'c' or i == 'C':
            a = list_string.remove(i)
    list_string = ''.join([str(i) for i in list_string])
    return list_string
    '''


def no_c(my_string):
    return "".join([i for i in my_string if i not in "cC"])
