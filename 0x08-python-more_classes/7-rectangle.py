#!/usr/bin/python3
''''

'''


class Rectangle:
    '''
    The class implementation
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width mus be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value