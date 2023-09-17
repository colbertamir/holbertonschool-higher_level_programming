#!/usr/bin/python3
# 3-safe_print_division.py
# Divides 2 integers and prints the result
def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Result: {}".format(div))
    return (div)
