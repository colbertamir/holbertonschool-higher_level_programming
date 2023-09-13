#!/usr/bin/python3
# 8-simple_delete.py
# Deletes a key in a dictionary
def simple_delete(a_dictionary, key=""):
     
    if not a_dictionary:
        return a_dictionary

    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
