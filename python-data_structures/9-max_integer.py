#!/usr/bin/python3
# 9-max_integer.py
# Finds biggest integer
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_integer = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > max_integer:
            max_integer = my_list[i]

            return max_integer
