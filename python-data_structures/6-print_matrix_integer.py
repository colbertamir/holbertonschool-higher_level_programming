#!/usr/bin/python3
# 6-print_matrix_integer.py
# Prints a matrix
def print_matrix_integer(matrix=[[]]):
    
    if not matrix:
        return

    for row in matrix:
        for col in row:
            print(f"{col:d}", end=" ")
        print()
