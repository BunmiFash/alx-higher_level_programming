#!/usr/bin/python3

"""A module that prints a square"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size: Size length of the square
    Raises:
        TypeError if anything other than an integer is passed
        ValueError if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    i = 0
    while i < size:
        print("#" * size)
        i += 1
