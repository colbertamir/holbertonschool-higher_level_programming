#!/usr/bin/python3
""" Defines Rectangle """


class Rectangle:
    """ Represents a Rectangle with Height and Width and added public class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":

    my_rectangle = Rectangle(4, 3)
    print("Area:", my_rectangle1.area())
    print("Perimeter:", my_rectangle1.perimeter())
    my_rectangle1.my_print()

    my_rectangle2 = Rectangle(2, 2)
    print("Area:", my_rectangle2.area())
    print("Perimeter:", my_rectangle2.perimeter())
    my_rectangle2.my_print()

    del my_rectangle1  # This will trigger the __del__ method
    del my_rectangle2

    print("Number of instaances:", Rectangle.number_of_instances)
