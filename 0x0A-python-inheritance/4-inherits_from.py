#!/usr/bin/python3

"""Defines `inherits_from` that checks object inherits from a class"""


def inherits_from(obj, a_class):
    """
    Return:
        True if @obj is instance of a class inherited from @a_class
        else:
            False
    Args:
        @obj: object being checked
        @a_class: specified class
    """
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
