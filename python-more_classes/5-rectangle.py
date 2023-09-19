#!/usr/bin/python3
""" Defines Rectangle """


class Rectangle:
    """ Represents a Rectangle with Height and Width attributes """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
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
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")


if __name__ == "__main__":

    my_rectangle = Rectangle(4, 3)
    print("Area:", my_rectangle.area())
    print("Perimeter:", my_rectangle.perimeter())
    my_rectangle.my_print()

    del my_rectangle  # This will trigger the __del__ method
