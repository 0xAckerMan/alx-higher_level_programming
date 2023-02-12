#!/usr/bin/python3
'''
class base
'''


class Base:
    ''' class implementation'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Class constructor
        ARGS:
            id which is setted to None
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
