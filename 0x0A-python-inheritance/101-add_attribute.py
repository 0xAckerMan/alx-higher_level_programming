#!/usr/bin/python3
"""
contains `add_attribute` function
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible
    Args:
        @obj: object added to
        @attr: name of the attribute
        @value: value of the attribute
    """
    if "__dict__" in dir(obj) and isinstance(obj.__dict__, dict):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
