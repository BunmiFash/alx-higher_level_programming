#!/usr/bin/python3

"""Module 12-pascal_triangle
Creates a pascal triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    pascal_tri = [[1]]
    for i in range(n - 1):
        pas = [1]
        for v in range(i):
            pas.append(pascal_tri[-1][v] + pascal_tri[-1][v + 1])
        pas.append(1)
        pascal_tri.append(pas)
    return pascal_tri
