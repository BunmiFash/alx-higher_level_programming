#!/usr/bin/python3

"""Module that inverts == and != operators"""


class MyInt(int):
    """MyInt inherits from the int class"""
    def __init__(self, value):
        """Initializing value"""
        self.value = value

    def __eq__(self, other):
        """Returns the inverse of original operation"""
        return self.value != other

    def __ne__(self, other):
        """Returns the inverse of original operation"""
        return self.value == other
