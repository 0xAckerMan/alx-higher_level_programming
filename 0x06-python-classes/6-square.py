#!/usr/bin/python3
'''Creating a class square'''


class Square:
    '''Implementation of the class'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or \
            len(position) != 2 or \
                not all(isinstance(num, int) for num in position) or \
                not all(num > 0 for num in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        """prints a square  with the corresponding size
        """
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
