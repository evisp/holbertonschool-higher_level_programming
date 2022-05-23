#!/usr/bin/python3

def matrix_divided(matrix, div):
    result = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(value / div, 2) for value in row] for row in matrix]
