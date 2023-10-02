#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Base class for managing id attributes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class.

        Args:
        id (int, optional): An int identifier. If provided, it is assigned to
        the 'id' attribute. If 'None', a new
        'id' is created by incrementing '__nb_objects' counter.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
