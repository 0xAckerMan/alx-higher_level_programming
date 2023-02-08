#!/usr/bin/python3
"""
Module contains `BaseGeometry` class
"""


class BaseGeometry:
    """
    Base class for geometry objects
    """

    def area(self):
        """
        Calculates area of the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if @value is an integer or not
        Args:
            @name: objects name(str)
            @value: integer(int)
        Raises:
            TypeError: if @value is not an integer
            ValueError: if @value <= 0
        """
        self.name = name
        self.value = value
        if not isinstance(self.value, int):
            raise TypeError(f"{self.name} must be an integer")
        elif self.value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
