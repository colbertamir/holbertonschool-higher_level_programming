#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

        Args:
            obj: The object being checked
            a_class: The class the obj is paired with.

        Returns:
            If obj isinstance or inherited - True \
                    otherwise False
    """
    return isinstance(obj, a_class)
