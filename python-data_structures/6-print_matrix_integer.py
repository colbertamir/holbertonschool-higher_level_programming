#!/usr/bin/python3
# 6-print_matrix_integer.py
# Prints a matrix
def print_matrix_integer(matrix=[[]]):
    
    if not matrix:
        return

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str.format("{0:d}", matrix[i][j]), end= " ")
        print()
