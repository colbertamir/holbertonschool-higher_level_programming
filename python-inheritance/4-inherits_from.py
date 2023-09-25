#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check
        a_class: The class paired with obj

    Returns:
        If obj is a inherited instance of a_class - True.
        Otherwise -False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
