#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ Instantiation Size and Raised exceptions """
    def __init__(self, size=0):
        self.__size = size
    if not isinstance(size, int)
    raise: TypeError(size must be an integer)
    elif < 0
    raise: ValueError(size must be >= 0)
