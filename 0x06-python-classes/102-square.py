#!/usr/bin/python3

""" A square class is defined"""


class Square:
    """ The method creates a private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size

    """ This method retireves the value of __size"""
    @property
    def size(self):
        return self.__size

    """ This method sets the value of __size"""
    @size.setter
    def size(self, value):
        if not type(value) is int or not type(value) is float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Area Method that returns the area of the square"""
    def area(self):
        return self.__size ** 2

    """ Method that compares <= """
    def __le__(self, other):
        return self.area() <= other.area()

    """ Method that compares < """
    def __lt__(self, other):
        return self.area() < other.area()

    """ Method that compares >= """
    def __ge__(self, other):
        return self.area() >= other.area()
    """ Method that compares != """
    def __ne__(self, other):
        return self.area() != other.area()
    """ Method that compares > """
    def __gt__(self, other):
        return self.area() > other.area()
    """ Method that compares == """
    def __eq__(self, other):
        return self.area() == other.area()
