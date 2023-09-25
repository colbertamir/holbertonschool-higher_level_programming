#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: The object to check
        a_class (type): The class to pai with obj

    Returns:
        If obj is exactly an instance of a_class will be True \
                otherwise False
    """
    return type(obj) is a_class
