#!/usr/bin/python3
'''
A continuation of advancing the Base geometry class
'''


class BaseGeometry:
    '''Class implementation'''

    def area(self):
        """
        Calculates area of the geometry
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check value
        Args:
            name (str): value designation
            value (any): value to check
        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """

        self.name = name
        self.value = value

        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
