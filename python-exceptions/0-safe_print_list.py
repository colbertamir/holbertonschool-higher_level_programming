#!/usr/bin/python3
# 0-safe_print_list.py
# Prints 'x' elements of a list
def safe_print_list(my_list=[], x=0):
    full_len = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            full_len += 1
        except IndexError:
            break
        return (full_len)
