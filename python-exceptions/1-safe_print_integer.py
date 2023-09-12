#!/usr/bin/python3
# 1-safe_print_integer.py
# Prints an integer with "{:d}".format().
def safe_print_integer(value):
    Args:
        value (int): The integer to print.

        Returns:
             If a TypeError or ValueError occurs - False.
             Otherwise - True.
        try:
            print("{:d}".format(value))
            return (True)
        except (TypeError, ValueError):
            return (False)
