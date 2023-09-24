#!/usr/bin/python3
def lookup(obj):
    """
    Get a list of public attributes and methods of an object.

    Args:
        obj: The object being inspected

    Returns:
        A list of public attributes/method names
    """

    try:
        attributes_and_methods = dir(obj)

        filtered_attributes_and_methods =
        [item for item in attributes_and_methods if not item.startswith("_")]

        return filtered_attributes_and_methods
    except TypeError:

        return []
