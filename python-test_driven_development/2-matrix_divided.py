#!/usr/bin/python3
"""
    Divides every element of a matrix
    2-matrix_divided.py

"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The number by which to divide every element of the
        matrix

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
            if each row in the matrix isn't the same size, or if div is not
            an int or float.

        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with all elements divided by div,
        rounded to two decimal places.

    """

    if (
            not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise
    TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise
    TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
