#!/usr/bin/python3

"""A module that returns the sum of two numbers

"""


def add_integer(a, b=98):
    """Return: The sum of two numbers.
    Args:
    a:
        The first number
    b:
        The second number
    Raises:
        TypeError, if a or b is neither a float or int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
