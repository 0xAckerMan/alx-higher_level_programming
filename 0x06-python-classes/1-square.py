#!/usr/bin/python3
'''Defines a class square and initializes its size'''


class Square:
    ''' class implementation
    '''
    def __init__(self, size):
        """
        Args:
            size: size of the square.
        Attributes:
            size: Private instance attribute.
        """
        self.__size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
