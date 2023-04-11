#!/usr/bin/python3


"""Module that checks for class instance"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class"""
    if (type(obj) == a_class):
        return True
    return False
