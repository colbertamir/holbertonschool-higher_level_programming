#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ Instantiation Size and Raised exceptions """

    def __init__(self, size=0):

        def size(self):
            return self.__size

        def size(self, value: int):
            self.__size = value

            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

            def area(self):
                return self.__size**2