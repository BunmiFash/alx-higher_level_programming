#!/usr/bin/python3

"""A module that divides a matrix by an int
and returns a new matrix

"""


def matrix_divided(matrix, div):
    """Return:
        A new matrix after dividing the original with an integer or float

    Args:
        matrix: Matrix to be divided. List of lists of int or float
        div: Divider

    Raises:
        TypeError:
            if matrix is not list of int or float
            if div is not a number
            if each row length is not equal to another
        ZeroDivisionError:
            if div == 0
    """
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    matrix_length = len(matrix)
    i = 0
    while True:
        if i == (matrix_length) - 1:
            break
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            pass
        i += 1

    for row in matrix:
        row_list = []
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            res = x / div
            res = float("{:.2f}".format(res))
            row_list.append(res)
        new_matrix.append(row_list)
    return new_matrix
