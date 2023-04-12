#!/usr/bin/python3

"""Module that inverts == and != operators"""


class MyInt(int):
    """MyInt inherits from the int class"""
    def __eq__(self, value):
        """Returns the inverse of original operation"""
        return self.real != value

    def __ne__(self, value):
        """Returns the inverse of original operation"""
        return self.real == value
