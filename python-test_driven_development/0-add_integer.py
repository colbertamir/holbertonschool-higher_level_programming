#!/usr/bin/python3
"""

0.add_integer
Method used to add ints

"""


def add_integer(a, b=98):
    """ Returns a & b as ints """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)

    return result
