#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Prints the first 'x' elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

        Returns:
            ret = 0
            for i in range(0, x):
                try:
                     print("{:d}".format(my_list[i]), end="")
                     ret += 1
                except (ValueError, TypeError):
                    continue
                print("")
                return (ret)
