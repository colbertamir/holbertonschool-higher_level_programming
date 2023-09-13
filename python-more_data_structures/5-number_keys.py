#!/usr/bin/python3
# 5-number_keys.py
# Returns the number of keys in a dictionary
def number_keys(a_dictionary):
    
    if not a_dictionary:
        return 0

    return len(a_dictionary.keys())
