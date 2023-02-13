#!/usr/bin/python3
'''
This module create a class rectangle that inherits from base
'''
from models.base import Base


class Rectangle(Base):
    '''
    The class
    Args: class Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Class constructor
        Args:
            width
            height
            id, x and y
        '''

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width getter'''

        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''

        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        '''Height  getter'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Height attribute setter method'''

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        '''X attribute getter method'''

        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method for x attribute'''

        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        '''getter method for the y attribute'''

        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method for the y attribute'''

        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
