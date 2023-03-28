#!/usr/bin/python3

""" A square class is defined"""


class Square:
    def __init__(self, size):
        """ This is the init method that defines a private attribute size

        Args:
            size(int): The size attribute of the square
        """
        self.__size = size  # A private instance attribute size
