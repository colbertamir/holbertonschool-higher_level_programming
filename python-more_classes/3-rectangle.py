#!/usr/bin/python3
""" Defines Rectangle """


class Rectangle:
    """ Becomes Rectangle with a Height and Width attribute """

    def __init__(self, width=0, height=0):
        self.height = height

        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def my_print(self):
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for _ in range(self.__height):
                print("#" * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])


if __name__ == "__main__":

    my_rectangel = Rectangle(4, 3)
    print("Area:", my_rectangle.area())
    print("Perimeter:", my_rectangle.perimeter())
    my_rectangle.my_print()
