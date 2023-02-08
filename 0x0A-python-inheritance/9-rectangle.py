#!/usr/bin/python3
'''class rectange, inherits from 7 geometry'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''The class implemrntation'''

    def __init__(self, width, height):
        '''The func impementation'''

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[{}] {}/{}'\
            .format(__class__.__name__, self.__width, self.__height)
