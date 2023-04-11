#!/usr/bin/python3

"""A module that lists all te attributes nad methods
of an object
"""


def lookup(obj):
    """A function that returns the list of available attributes
    and methods of an object
    Args:
        obj: Object whose attributes and methods are returned

    Returns: List of all attributes and methods
    """
    obj = dir(obj)
    return obj
