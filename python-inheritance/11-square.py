#!/usr/bin/python3
""" Defines a Square a subclass of a Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size):
        """Initializes Square.

        Args:
            size (int): The size of a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
