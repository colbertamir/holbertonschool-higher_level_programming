#!/usr/bin/python3
"""Defines inherited class MyList."""


class MyList(list):
    """Inherited class MyList from built-in class list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(4)
    my_list.append(2)
    my_list.append(7)
    my_list.print_sorted()
