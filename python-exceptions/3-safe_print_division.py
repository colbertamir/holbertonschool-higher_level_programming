#!/usr/bin/python3
# 3-safe_print_division.py
# Divides 2 integers and prints the result
def safe_print_division(a, b):
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    try:
        div = a / b
    except ZeroDivisionError:
        div = None

        print("Inside result: {}".format(div))
         return (div)
