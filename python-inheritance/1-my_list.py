#!/usr/bin/python3
"""Defines an inherited class called MyList"""


class MyList(list):
    """ Adding sorted printing for built-in class """

    def print_sorted(self):
        """ Prints a list in ascending sorted order """
        print(sorted(self))
