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
