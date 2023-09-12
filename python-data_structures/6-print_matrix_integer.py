#!/usr/bin/python3
# 6-print_matrix_integer.py
# Prints a matrix
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}", end=" ")
        print()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print_matrix_integer(matrix)
