#!/usr/bin/python3
"""Defines an inherited class called MyList"""


class MyList(list):
    """ Inherited class Mylist from built-in class list """

    def print_sorted(self):
        """ Prints a list sorted in ascending order """
        print(sorted(self))
