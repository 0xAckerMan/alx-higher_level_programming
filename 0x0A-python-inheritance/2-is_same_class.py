#!/usr/bin/python3
'''Checks obj isinstace of the specified class'''


def is_same_class(obj, a_class):
    '''
    Args:
        obj and a_class
    Returns
        true or false
    '''

    if type(obj) == a_class:
        return True
    return False
