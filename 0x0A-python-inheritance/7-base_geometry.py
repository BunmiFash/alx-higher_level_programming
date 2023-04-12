#!/usr/bin/python3


"""Module that creates a Base Class"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value"""
        if (type(value) is not int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
