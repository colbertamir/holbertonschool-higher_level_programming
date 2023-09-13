#!/usr/bin/python3
# 2-uniq_add.py
# Adds all unique integers in a list (only once for each integer)
def uniq_add(my_list=[]):
    if not my_list:
        return 0

    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

        return (num)
