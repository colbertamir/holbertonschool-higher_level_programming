#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specific class.

    Args:
        obj: The object checked.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of the specific class,\
                False otherwise.
    """
    return type(obj) is a_class
