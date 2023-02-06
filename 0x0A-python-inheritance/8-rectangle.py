#!/usr/bin/python3
"""
Module that inherits `BaseGeometry` class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Geometry object from inherited class BaseGeometry
    """

    def __init__(self, width, height) -> None:
        """
        initialize new rectangle geometry object
        with given @height nad @width
        Args:
            @height: height of the rectangle
            @width: width of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
