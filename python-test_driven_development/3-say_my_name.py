#!/usr/bin/python3
"""
3-say_my_name.py
Prints name in first name last name format

"""


def say_my_name(first_name, last_name=""):
    """

    Args:
        first_name (st): first name
        last_name (str, optional): last name. Default - "".

    """
    if not isinstance(first_name, str):
        raise
    TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = f"My name is {first_name} {last_name}" if last_name\
        else f"My name is {first_name}"
    print(full_name)
