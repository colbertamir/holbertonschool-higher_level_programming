#!/usr/bin/python3
# 4-new_in_list.py
# Replaces element at specific position w/o modifying original list
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [e for e in my_list]
    copy[idx] = element
    return(copy)
