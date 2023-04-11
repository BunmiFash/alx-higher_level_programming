#!/usr/bin/python3

"""Module that checks if an object is an instance of a class or child class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or its Child class"""
    return isinstance(obj, a_class)
