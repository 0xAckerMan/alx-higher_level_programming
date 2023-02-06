#!/usr/bin/python3
'''
A continuation of advancing the Base geometry class
'''


class BaseGeometry:
    '''Class implementation'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        elif value < 0:
            raise ValueError("{} must be greater than 0".format(value))
