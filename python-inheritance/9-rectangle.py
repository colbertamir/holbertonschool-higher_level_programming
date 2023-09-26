#!/usr/bin/python3
"""Defines a class called Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def __str__(self):
            """Return the print() and str() representation of a Rectangle."""
            string = "[" + str(self.__class__.__name__) + "]"
            string += str(self.__width) + "/" + str(self.__height)
            return string
