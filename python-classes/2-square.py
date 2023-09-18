#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ Instantiation Size and Raised exceptions """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size