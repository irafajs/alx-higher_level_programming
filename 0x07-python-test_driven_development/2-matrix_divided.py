#!/usr/bin/python3
"""doc"""
message = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """divided matrix by a div"""
    mat = []
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        new_mat = []
        for j in range(len(matrix[i])):
            a = matrix[i][j] / div
            new_mat.append(round(a, 2))
        mat.append(new_mat)
    return mat
