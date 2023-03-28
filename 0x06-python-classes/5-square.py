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
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Area Mthod that returns the area of the square"""
    def area(self):
        return self.__size ** 2

    """ This method prints a square with # """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        sqr = self.__size
        while (sqr > 0):
            for i in range(self.__size):
                print("#", end='')
            print()
            sqr -= 1
