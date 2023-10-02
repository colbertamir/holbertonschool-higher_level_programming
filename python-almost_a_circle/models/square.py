#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The identity of the square.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string version of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square.

        Args:
            *args (int): Attribute values.
                1st arg represents id attribute
                2nd arg represents size attribute
                3rd arg represents x attribute
                4th arg represents y attribute
            **kwargs (dict): Key-value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is not None:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is not None:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary version of Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
