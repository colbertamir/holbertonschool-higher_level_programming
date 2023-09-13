#!/usr/bin/python3
# 6-print_matrix_integer.py
# Prints a matrix
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print(f"{col:d}", end=" ")
        print()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print_matrix_integer(matrix)
