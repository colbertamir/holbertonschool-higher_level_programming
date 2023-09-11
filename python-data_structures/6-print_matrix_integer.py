#!/usr/bin/python3
# 6-print_matrix_integer.py
# Prints a matrix
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for e in row:
            print("{:d}".format(e), end= if e != row[-1] else "")
            print()
