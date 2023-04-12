#!/usr/bin/python3

"""Module that adds an attribute to an object, if possible"""


def add_attribute(obj, attr, value):
    """Adds an attribute to an object if possible"""
    if ("__dict__" in dir(obj)):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
