#!/usr/bin/python3
''' Class rectangle with __del__'''


class Rectangle():
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
            raise ValueError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__self

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise ValueError("height must be an integer")
        elif value < 0:
            ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)

    def __str__(self):
        output = ''
        if self.__width == 0 or self.__height == 0:
            return output
        for i in range(self.__height):
            output += '#' * self.__width
            if i != self.__height - 1:
                output += '\n'
        return output

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print('Bye rectangle...')
