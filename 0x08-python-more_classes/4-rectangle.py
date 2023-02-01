#!/usr/bin/python3
'''
A class rectangle
Has private instances: Width and height
public instances methods: Area and Perimeter
str and repr with eval()
'''


class Rectangle():
    '''The class implementation'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        total = ''
        if self.__height == 0 or self.__width == 0:
            return total
        for _ in range(self.__height):
            total += '#' * self.__width
            if _ != self.__height - 1:
                total += '\n'
        return total

    def __repr__(self):
        return f"Rectangle ({self.__width}, {self.__height})"
