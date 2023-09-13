#!/usr/bin/python3
# 0-safe_print_list.py
# Prints 'x' elements of a list
def safe_print_list(my_list=[], x=0):
    
    if not my_list:
        return 0

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            print("The list has only {} elements.".format(len(my_list)))
            break
        print("")
        return (ret)
