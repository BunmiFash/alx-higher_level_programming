#!/usr/bin/python3

""" A square class is defined"""


class Square:
    """ The method creates a private instance attribute size"""
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ Area Mthod that returns the area of the square"""
    def area(self):
        return self.__size ** 2
