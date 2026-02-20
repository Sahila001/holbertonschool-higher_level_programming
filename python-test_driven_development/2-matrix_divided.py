#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div"""

    # Check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check matrix structure
    if (not isinstance(matrix, list) or
            matrix == [] or
            any(not isinstance(row, list) for row in matrix) or
            any(not all(isinstance(elem, (int, float)) for elem in row)
                for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check rows size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    # Return new divided matrix rounded to 2 decimals
    return [[round(elem / div, 2) for elem in row] for row in matrix]
