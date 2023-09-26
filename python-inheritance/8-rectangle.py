#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes a new Rectangle.

        Args:
            width: The width of Rectangle
            height: The height Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.__width = 0
        self.__height = 0
    
    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
