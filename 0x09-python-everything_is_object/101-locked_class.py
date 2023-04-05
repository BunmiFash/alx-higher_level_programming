#!/usr/bin/python3

""" A module that prevents users from creating attributes"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ("first_name")
