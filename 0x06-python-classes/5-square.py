#!/usr/bin/python3
'''
Implementation of the square class
'''


class Square:
    ''' Class implementation'''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Calc square area'''
        return (self.__size ** 2)

    def my_print(self):
        '''Prints a square'''
        if (self.__size == 0):
            print('')

        for _ in range(self.__size):
            print("#" * self.__size)
