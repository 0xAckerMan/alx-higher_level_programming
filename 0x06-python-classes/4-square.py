#!/usr/bin/python3
'''
Defines a class sqaure checks its attribute with
area func
'''


class Square:
    ''' The class implementation'''
    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self):
            if type(size) != int:
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            self.__size = size

        def area(self):
            return (self.__size ** 2)
